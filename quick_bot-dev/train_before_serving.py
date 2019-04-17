from src.utils import constant, io_utils
from src.nlp_lib import ridge_classifier
import pandas as pd
import traceback

for lang in constant.SUPPORT_LANGUAGES:
    try:
        model = ridge_classifier.IntentRidgeClassifier()
        # Load data train

        df_train = pd.read_excel(constant.MODEL_INFO.get(lang).get(constant.DATA_TRAIN_PATH), sheet_name='Sheet1')
        # Make dict label to answer

        intent_lists = df_train['INTENT'].unique()
        dict_intent_2_answer = {intent: df_train[df_train['INTENT'] == intent].iloc[0]['ANSWER'] for intent in
                                intent_lists}
        io_utils.save_dict_to_file(dict_intent_2_answer, constant.MODEL_INFO.get(lang).get(constant.DICT_ANSWER_PATH))

        x_train_raw, y_train_raw = df_train['SAMPLE'].values, df_train['INTENT'].values
        # Init model
        model.set_data_train(x_train_raw, y_train_raw, lang)
        model.build_model()
        model.train_model()

        # save data
        model.save_model(constant.MODEL_INFO.get(lang).get(constant.MODEL_PATH))
        model.save_dict_labels(constant.MODEL_INFO.get(lang).get(constant.DICT_2_LABEL_PATH))
        model.save_word2index(constant.MODEL_INFO.get(lang).get(constant.WORD_2_INDEX_PATH))
    except:
        print('Error when train model with language: ', lang)
        traceback.print_exc()
        pass
