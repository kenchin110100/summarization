# coding: utf-8
"""
文の操作をするためのクラス
"""
import MeCab
import numpy as np


class Sentence:

    def __init__(self, neologd_path=None):
        if neologd_path is not None:
            self.neologd_path = "-d " + neologd_path
        else:
            self.neologd_path = ""

    # 形態素解析済みの文章をベクトルにするための関数
    def sentence_to_vector(self, list_word, dict_word_to_vector):
        # ワードベクトルを用いた行列の作成
        arr_vector = None
        for word in list_word:
            try:
                if arr_vector is None:
                    arr_vector = dict_word_to_vector[word]
                else:
                    arr_vector = np.vstack((arr_vector,
                                            dict_word_to_vector[word]))
            except KeyError:
                pass
            except Exception as e:
                print '=== エラー内容 ==='
                print 'type:' + str(type(e))
                print 'args:' + str(e.args)
                print 'message:' + e.message
                print 'e自身:' + str(e)
        # ベクトル作成ができない場合はNoneを返す
        if arr_vector is None:
            return None
        # mean, max, minでリストを作成
        sentence_vector = []
        for i in range(arr_vector.shape[1]):
            sentence_vector.extend([np.mean(arr_vector[:, i]),
                                    np.max(arr_vector[:, i]),
                                    np.min(arr_vector[:, i])])

        return sentence_vector

    # 文章を形態素解析して、リストにする
    def sentence_owakati(self, sentence):
        tagger = MeCab.Tagger('-Owakati ' + self.neologd_path)
        # お分かちして、リスト化する
        result = tagger.parse(sentence).split(' ')
        # 改行コードを削除
        if '\n' in result:
            result.remove('\n')

        return result

    # １つの文章を「。」で分割して、リストに変更する
    def separate_sentence(self, sentence):
        list_sentence = sentence.split("。")
        # 改行コードや、空集合を削除する
        if '\n' in list_sentence:
            list_sentence.remove('\n')
        elif '' in list_sentence:
            list_sentence.remove('')

        return list_sentence
