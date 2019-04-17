HISTORY_DIR = 'history/'

LANG_JP = 'jp'
LANG_VN = 'vi'
LANG_ENG = 'en'
SUPPORT_LANGUAGES = [LANG_JP, LANG_VN]
NOT_SUPPORT_LANGUAGE = "not_support"

MODEL_PATH = 'model_path'
DICT_2_LABEL_PATH = 'dict2label_path'
WORD_2_INDEX_PATH = 'word2index_path'
DATA_TRAIN_PATH = 'data_train_path'
DICT_ANSWER_PATH = 'intent2answer_path'
MODEL_THRESHOLD = 'threshold'

#FWI_Chatbot_ThanhVuong
FB_AT_WORK_API = 'https://graph.facebook.com/v2.6/me/messages'
FB_AT_WORK_ACCESS_TOKEN = 'DQVJ2ZADhrRnVHM3lxRDRFSExnMThIallyMkJIRVBCRl9HR1JpRTJJRVZACcWUyRnktNFNyME53TFU5OGtKUXlZAWWFYVEhielQzMXIzNGdKVHk0NjhGQVhqZAEV0U2ZAuMHZAQRm1QWm1uTm1yWGtVd1NjNV9Qd1dJaU5pd3k4VUtHRzZAUdFJjOTNuQ1BDc1Q3bjVkWnFUdTdVN01QMWlUZAWFVNmxqWjlZATGl0bzdrM1dhY3NjS2hJLXYtaUk1SkI5RF9LQXlUakF3UkQ4dmJMUU1IVQZDZD'
FB_AT_WORK_VERIFY_TOKEN = 'fpt123567123'

DEFAULT_ANSWER = {
    LANG_JP: "Chúng tôi chưa hỗ trợ nội dung bạn hỏi. Vui lòng hỏi câu hỏi khác",
    LANG_VN: "Chúng tôi chưa hỗ trợ nội dung bạn hỏi. Vui lòng hỏi câu hỏi khác",
    LANG_ENG: "Chúng tôi chưa hỗ trợ nội dung bạn hỏi. Vui lòng hỏi câu hỏi khác",
    NOT_SUPPORT_LANGUAGE: "Your language is not support yet"
}
# sample_for_chatbot_end_jpn.xlsx
MODEL_INFO = {
    LANG_JP: {
        MODEL_PATH: 'models/jp/model.pickle',
        DICT_2_LABEL_PATH: 'models/jp/int_2_label.txt',
        WORD_2_INDEX_PATH: 'models/jp/word_2_index.txt',
        DATA_TRAIN_PATH: 'models/jp/sample_for_chatbot_end_jpn.xlsx',
        DICT_ANSWER_PATH: 'models/jp/intent_2_answer.txt',
        MODEL_THRESHOLD: 0.7

    },
    LANG_VN: {
        MODEL_PATH: 'models/vn/model.pickle',
        DICT_2_LABEL_PATH: 'models/vn/int_2_label.txt',
        WORD_2_INDEX_PATH: 'models/vn/word_2_index.txt',
        DATA_TRAIN_PATH: 'models/vn/sample_for_chatbot_end.xlsx',
        DICT_ANSWER_PATH: 'models/vn/intent_2_answer.txt',
        MODEL_THRESHOLD: 0.8
    }, LANG_ENG: {
        MODEL_PATH: 'models/en/model.pickle',
        DICT_2_LABEL_PATH: 'models/en/int_2_label.txt',
        WORD_2_INDEX_PATH: 'models/en/word_2_index.txt',
        DATA_TRAIN_PATH: 'models/en/sample_for_chatbot_end_eng.xlsx',
        DICT_ANSWER_PATH: 'models/en/intent_2_answer.txt',
        MODEL_THRESHOLD: 0.7
    }
}
