from flask import Flask
from flask import request
from src.utils import facebook_utils
from langdetect import detect
from src.utils import constant, io_utils
from src.nlp_lib.ridge_classifier import IntentRidgeClassifier

app = Flask(__name__)

#hello
def detect_message(text):
    try:
        language = detect(text)
        print('language: ', language)
        return language
    except:
        return None


@app.route('/messenger/chat', methods=['GET', 'POST'])
def handle_messenger_request():
    if request.method == 'GET':
        return facebook_utils.verify_token(request)
    elif request.method == 'POST':
        json_request = request.get_json()
        print(json_request)
        list_message_info = facebook_utils.message_info_from_request(json_request)
        if list_message_info is None:
            return ''

        for message_info in list_message_info:
            recipient_id = message_info.sender_id
            text_question = message_info.text_message
            language = detect_message(text_question)
            if language not in constant.SUPPORT_LANGUAGES:
                answer = constant.DEFAULT_ANSWER.get(constant.NOT_SUPPORT_LANGUAGE)
            else:
                word2index = io_utils.read_dicts_from_file(
                    constant.MODEL_INFO.get(language).get(constant.WORD_2_INDEX_PATH))
                int2label = io_utils.read_dicts_from_file(
                    constant.MODEL_INFO.get(language).get(constant.DICT_2_LABEL_PATH))
                intent2answer = io_utils.read_dicts_from_file(
                    constant.MODEL_INFO.get(language).get(constant.DICT_ANSWER_PATH))
                pretrain_model_path = constant.MODEL_INFO.get(language).get(constant.MODEL_PATH)

                model = IntentRidgeClassifier()
                model.set_word2index(word2index)
                model.set_dict_labels(int2label)
                model.load_model(pretrain_model_path)

                result = model.predict(text_question)
                print(result['prob'])

                if result is not None and result['prob'] >= constant.MODEL_INFO.get(language).get(
                        constant.MODEL_THRESHOLD):
                    answer = result['intent']
                    answer = intent2answer[answer]
                else:
                    answer = constant.DEFAULT_ANSWER.get(language)

            facebook_utils.response_answer_to_fb(recipient_id, answer)
            io_utils.save_history(question=text_question, answer=answer)
    return 'Ok', 200


if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True, port=5000, threaded=True, use_reloader='True')
