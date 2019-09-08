import os
import math
from pprint import pprint as pp

file_path = './data'


def get_doc_tf(doc_name):
    """获取指定文档的词频字典.

    :param doc_name: 文档名称
    :return:
    """
    word_tf = dict()
    with open(doc_name, 'r', encoding='utf-8') as f:
        for line in f:
            for word in line.split():
                word_cnt = word_tf.get(word, 0)
                word_tf[word] = word_cnt + 1

    tot_word_num = 0
    for word in word_tf:
        tot_word_num += word_tf.get(word, 0)

    for word in word_tf:
        word_tf[word] = float(word_tf.get(word, 0)) / tot_word_num

    return word_tf


def get_all_docs_word_frequency(path_name):
    """获取指定目录下所有文档的词频

    :param path_name: 路径名称
    :return:
    """
    all_doc_word_freq = dict()
    for doc_name in os.listdir(path_name):
        doc_pth_name = os.path.join(path_name, doc_name)
        all_doc_word_freq[doc_name] = get_doc_tf(doc_pth_name)

    return all_doc_word_freq


def get_all_words_freq(docs_word_freq):
    """获取语料库中所有单词的词频

    :param docs_word_freq: 各个文档的词频.
    :return:
    """
    all_word_freq = {}
    for doc in docs_word_freq:
        doc_word_freq = docs_word_freq.get(doc, {})
        for word in doc_word_freq:
            word_freq = all_word_freq.get(word, 0) + doc_word_freq.get(word, 0)
            all_word_freq[word] = word_freq

    return all_word_freq


def get_word_doc_freq(all_doc_word_freq):
    """计算语料库中的每个单词在多少篇文档中出现（doc_frequency）。

    :param all_doc_word_freq:
    :return:
    """
    word_doc_freq = dict()
    for doc in all_doc_word_freq:
        word_freq_in_doc = all_doc_word_freq.get(doc, {})
        for word in word_freq_in_doc:
            doc_cnt = word_doc_freq.get(word, 0) + 1
            word_doc_freq[word] = doc_cnt

    return word_doc_freq


def get_num_of_docs_contains_word(all_doc_freq, word):
    """获取语料库中包含指定词语的文档个数.

    :param all_doc_freq:
    :param word:
    :return:
    """
    doc_num = 0
    for doc in all_doc_freq:
        if all_doc_freq.get(doc, {}).get(word, 0) > 0:
            doc_num += 1
    return doc_num


def get_all_words_idf(all_doc_freq, all_word_freq):
    """获取语料库中所有单词的idf值(反文档频率）。

    :param all_doc_freq: 语料库中各个文档中所有单词的词频。
    :param all_word_freq: 语料库所有单词的词频.
    :return:
    """
    word_idf = dict()
    doc_num = len(all_doc_freq)
    for word in all_word_freq:
        num_of_docs_contains_word = get_num_of_docs_contains_word(all_doc_freq, word)
        word_idf[word] = math.log(float(doc_num) / (num_of_docs_contains_word + 1))

    return word_idf


def get_all_doc_words_tf_idf(all_doc_word_freq, word_doc_freq):
    """计算语料库中各个文档中各个单词的tf-idf值。

    :param all_doc_word_freq:
    :param word_doc_freq:
    :return:
    """
    tf_idf_dict = dict()
    for doc in all_doc_word_freq:
        tf_idf_dict[doc] = {}

        for word in word_doc_freq:
            word_in_doc_freq = all_doc_word_freq.get(doc, {}).get(word, 0)
            all_doc_word_freq[doc][word] = word_in_doc_freq * word_doc_freq.get(word, 0)

    return all_doc_word_freq


if __name__ == '__main__':
    all_doc_word_freq = get_all_docs_word_frequency('./data')
    # all_word_freq = get_all_words_freq(all_doc_freq)
    # all_word_idf = get_all_words_idf(all_doc_freq, all_word_freq)
    word_doc_freq = get_word_doc_freq(all_doc_word_freq)
    tf_idf_dict = get_all_doc_words_tf_idf(all_doc_word_freq, word_doc_freq)
    pp(tf_idf_dict.get('5yule.seg.cln.txt', {}).get('毒'))
