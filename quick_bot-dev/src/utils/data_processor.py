import numpy as np
import MeCab


def japanese_segment(text):
    """
    Japanese text segment(Tokenize sequence)
    :param text: raw japanese text.
    :return: text after tokenize.
    """
    tagger = MeCab.Tagger("mecabrc")
    mecab_result = tagger.parse(text)
    tokens = []
    info_of_words = mecab_result.split("\n")
    for info in info_of_words:
        info = info.strip()
        if info == "EOS" or info == "":
            continue
        info_elems = info.split("\t")
        if len(info_elems) != 2:
            continue
        info_elems_right = info_elems[1].split(",")
        word = info_elems_right[6]
        if word == "*":
            word = info_elems[0]
        tokens.append(word)

    return " ".join(tokens)


def make_dict_labels(y_labels: np.array):
    """
    Build dict from data labels
    :param y_labels: array labels (Y in data train)
    :return: dict contain unique labels
    """
    if len(y_labels) == 0 or y_labels is None:
        return None
    try:
        _ = y_labels.shape[1]
        flatten = y_labels.flatten()
    except Exception:
        flatten = np.array([])
        for sample in y_labels:
            flatten = np.append(flatten, np.array(sample).flatten())
    labels = np.unique(flatten)
    dict_labels = {label: i for i, label in enumerate(labels)}
    return dict_labels


def label2vec(y_labels: np.array, dict_labels):
    """
    Convert raw label to vector with labels
    :param y_labels: data labels raw -> 1d label
    :param dict_labels: dict : {labels: int}
    :return: vector number corresponding
    """
    y_to_number = [dict_labels[label] for label in y_labels]
    return y_to_number


def word_2_index(word, dict_vocab: dict):
    try:
        return dict_vocab[word]
    except:
        return len(word)


def sentence_2_vec(sentence, dict_vocab, max_size):
    rs = np.zeros(max_size)
    rs[[word_2_index(word, dict_vocab) for word in sentence.split(' ')]] = 1
    return rs
