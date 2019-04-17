from sklearn.linear_model import RidgeClassifier
from src.utils import constant, data_processor, io_utils
import pickle
import numpy as np
import traceback


class IntentRidgeClassifier:

    def __init__(self):
        self.model = None
        self.x_train = None
        self.y_train = None
        self.language = None
        self.word2index = None
        self.dict_labels = None

    def set_word2index(self, word2index: dict):
        self.word2index = word2index

    def set_dict_labels(self, dict_labels: dict):
        self.dict_labels = dict_labels

    def set_data_train(self, x_raw, y_raw, language):
        if x_raw is None or y_raw is None or language is None:
            print('Data train is None')
            return
        self.x_train = x_raw
        self.y_train = y_raw
        self.language = language
        self.process_data()

    def process_data(self):
        # tokenize
        if self.language == constant.LANG_JP:
            self.x_train = [data_processor.japanese_segment(sentence) for sentence in self.x_train]

        # build vocab
        if self.word2index is None:
            unique_words = list(set([word for sentence in self.x_train for word in sentence.split(' ')]))
            self.word2index = {word: index for index, word in enumerate(unique_words)}

        # Convert data to vector
        self.x_train = [data_processor.sentence_2_vec(sentence, self.word2index, len(self.word2index) + 1) for sentence
                        in self.x_train]

        self.dict_labels = data_processor.make_dict_labels(self.y_train)
        self.y_train = data_processor.label2vec(self.y_train, self.dict_labels)

    def build_model(self):
        self.model = RidgeClassifier(alpha=0.5, class_weight=None, copy_X=True, fit_intercept=True, solver='svd', tol=1)

    def train_model(self):
        self.model.fit(self.x_train, self.y_train)

    def predict(self, x_raw):
        x_to_predict = data_processor.sentence_2_vec(x_raw, self.word2index, len(self.word2index) + 1)
        if sum(x_to_predict) == 0:
            return None
        d = self.model.decision_function([x_to_predict])[0] * 5
        probs = np.exp(d) / np.sum(np.exp(d))

        dict_labels = {self.dict_labels[key]: key for key in self.dict_labels.keys()}

        if len(dict_labels.keys()) < 3:
            final_rs = [{'intent': dict_labels[index], 'prob': probs} for index in range(1)]
            return final_rs[0]
        else:
            max_probability = np.argmax(probs)
        return {'intent': dict_labels[max_probability], 'prob': probs[max_probability]}

    def save_word2index(self, file_path):
        io_utils.save_dict_to_file(self.word2index, file_path)
        pass

    def save_model(self, model_path):
        if self.model is not None:
            with open(model_path, 'wb') as fw:
                pickle.dump(self.model, fw)
        else:
            print('Model is None.')

    def load_model(self, model_path):
        try:
            with open(model_path, 'rb') as fr:
                self.model = pickle.load(fr)
        except Exception:
            self.model = None
            print('Error when load model \n', traceback.format_exc())

    def save_dict_labels(self, file_path):
        io_utils.save_dict_to_file(self.dict_labels, file_path)
