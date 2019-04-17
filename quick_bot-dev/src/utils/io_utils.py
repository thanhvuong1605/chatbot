import os
import pickle
import traceback
from src.utils import constant
from datetime import datetime


def save_dict_to_file(dicts, file_path):
    """
    Save a dictionary to file.

    :param dicts: dict python
    :param file_path: path save dict
    :return: true if save success, otherwise, return false.
    """
    try:
        with open(file_path, 'w') as f:
            f.write(dicts.__str__())
    except IOError as e:
        print('Save failed : ', e)
        return False
    return True


def read_dicts_from_file(file_path):
    """
    Read dict from file. File path may depend on model name.
    :param file_path: path of dict
    :return: Return None if file not exits, otherwise, return dict contain labels.
    """
    try:
        with open(file_path, 'r', encoding='utf8') as f:
            seq = f.read()
            _dict = eval(seq)
    except Exception as e:
        print('Error when load dict: ', e)
        return None
    return _dict


def remove_file(file_path):
    try:
        if os.path.exists(file_path):
            os.remove(file_path)
        return True
    except IOError as e:
        print('Error when delete file', e)
        return False


def load_pickle(file_path):
    """
    Load pickle file from file path.

    :param file_path: path of file
    :return: pickle data from file path.
    """
    try:
        print('Load file: ', file_path)
        with open(file_path, 'rb') as fr:
            output = pickle.load(fr)
            return output
    except:
        print('Error when load pickle file: ', traceback.format_exc())
        return None


def save_pickle(data, file_path):
    """
    Save pickle file.
    :param data: data
    :param file_path: path of file
    :return: pickle data from file path.
    """
    try:
        print('Save data to file: ', file_path)
        with open(file_path, 'wb') as fw:
            pickle.dump(data, fw)
            print('Save file completed.')
            return True
    except:
        print('Error when save pickle file: ', traceback.format_exc())
        return False


def save_history(question, answer):
    """
    Save history to file.
    :param config: appconfig
    :param question: question
    :param answer: aswer
    :param user: user information
    :return:
    """
    try:
        history_dir = constant.HISTORY_DIR
        if not os.path.exists(history_dir):
            os.makedirs(history_dir)

        daily_log_path = history_dir + '/history_' + datetime.now().strftime("%Y_%m_%d") + '.txt'
        with open(daily_log_path, 'a', encoding='utf-8') as f:
            f.write('question: ' + str(question) + ' - answer: ' + str(answer) + '\n')

    except:
        print('Error when save history: \n', traceback.format_exc())
