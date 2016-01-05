# coding: utf-8
"""
文書要約のためのメインクラス
"""
import numpy as np
import ConfigParser
from functions.filer import Filer
from functions.sentence import Sentence
from functions.vector import Vector


class Summarization:
    def __init__(self, cluster, gamma, lamda):
        # クラスタ数
        self.K = cluster
        # ガンマの値
        self.gamma = gamma
        # ラムダの値
        self.lamda = lamda

        # configファイルの読み込み
        try:
            inifile = ConfigParser.ConfigParser()
            inifile.read("/var/www/cgi-bin/test_proj/summarization/files/config.ini")
            # 分散表現を記録したdictのパス
            self.dictpath = inifile.get('Dictionary', 'dictpath')
            self.neologdpath = inifile.get('Dictionary', 'neologdpath')

        except:
            self.dictpath = "/var/www/cgi-bin/test_proj/summarization/files/dict_word_to_vector_normalized.dump"
            self.neologdpath = "/usr/local/lib/mecab/dic/mecab-ipadic-neologd"
            

        # list_S
        self.list_S = None
        # 要約文
        self.list_sentence_S = None
        # 原文
        self.list_sentence_V = None

        # 各クラスのインスタンス化
        self.sentence = Sentence(self.neologdpath)

    @property
    def list_S(self):
        return None

    @list_S.setter
    def list_S(self, list_S):
        self.list_S = list_S

    @list_S.getter
    def list_S(self):
        return self.list_S

    @property
    def list_sentence_S(self):
        return None

    @list_sentence_S.setter
    def list_sentence_S(self, list_sentence_S):
        self.list_sentence_S = list_sentence_S

    @list_sentence_S.getter
    def list_sentence_S(self):
        return self.list_sentence_S

    @property
    def list_sentence_V(self):
        return None

    @list_sentence_V.setter
    def list_sentence_V(self, list_sentence_V):
        self.list_sentence_V = list_sentence_V

    @list_sentence_V.getter
    def list_sentence_V(self):
        return self.list_sentence_V

    # Ci_sを計算
    def _cal_Ci_s(self, i, arr_similarity, list_sentence_num):
        Ci_s = np.sum(arr_similarity[i][list_sentence_num])
        return Ci_s

    # C_Vを計算
    def _cal_C_V(self, arr_similarity):
        return np.sum(arr_similarity, axis=0)

    # L_Sを計算
    def _cal_L_S(self, list_sentence_num, arr_similarity, gamma, arr_C_V):
        list_L_S = [np.minimum(self._cal_Ci_s(i, arr_similarity,
                                              list_sentence_num),
                               gamma * arr_C_V[i])
                    for i in range(len(arr_C_V))]
        return sum(list_L_S)

    # R_Sを計算
    def _cal_R_S(self, list_sentence_num, list_sentence_labels):
        # いくつのクラスタが含まれているか計算
        R_S = set(list_sentence_labels[list_sentence_num])
        return len(R_S)

    # f_docを計算
    def _cal_f_doc(self, list_sentence_num, arr_similarity, arr_C_V,
                   list_sentence_labels, gamma, lamda):
        L_S = self._cal_L_S(list_sentence_num, arr_similarity, gamma, arr_C_V)
        R_S = self._cal_R_S(list_sentence_num, list_sentence_labels)
        f_doc = L_S + lamda * R_S

        return f_doc

    def cal_greedy(self, sentence, limit_sentence_num):
        # 要約文の累積単語数
        # word_num = 0
        # sentenceのリスト化
        list_sentence = self.sentence.separate_sentence(sentence)
        # 要約文のラベル集合
        list_S = []
        # 文書集合のラベル集合
        list_V = [i for i in range(len(list_sentence))]

        # 文を分かち書きする
        list_sentence_word = [self.sentence.sentence_owakati(sentence)
                              for sentence in list_sentence]
        # リストの文章をベクトルに置き換える
        dict_word_to_vector = Filer.readpickle(self.dictpath)
        list_sentence_vector = [self.sentence.sentence_to_vector(sentence_word,
                                                                 dict_word_to_vector)
                                for sentence_word in list_sentence_word]
        # 文間の類似度を計算
        arr_similarity = Vector.cal_similarity_matrix(list_sentence_vector)
        # C_Vを計算
        arr_C_V = self._cal_C_V(arr_similarity)
        # 文書をクラスタリング
        list_sentence_labels = Vector.cal_clustering(list_sentence_vector,
                                                     self.K)

        # 劣モジュラ関数の修正貪欲法
        # while limit_word_num > word_num:
        while len(list_S) < limit_sentence_num:
            # f_doc / c のスコアを記録するための変数
            score_tmp = 0
            # その時点で最高スコアを記録している文iを記録するための変数
            sentence_num_tmp = None

            for i in list_V:
                # 文iを１つずつ加えてf_docを計算
                list_S.append(i)
                f_doc = self._cal_f_doc(list_S,
                                        arr_similarity,
                                        arr_C_V,
                                        list_sentence_labels,
                                        self.gamma,
                                        self.lamda)
                # 計算後に文iを集合Sから除く
                list_S.pop()
                # f_doc / c がその時点の最高スコアなら記録
                """
                if f_doc / len(list_sentence_word[i]) > score_tmp:
                    score_tmp = f_doc / len(list_sentence_word[i])
                    sentence_num_tmp = i
                """
                if f_doc > score_tmp:
                    score_tmp = f_doc
                    sentence_num_tmp = i

            # 最高スコアを記録した文iを集合Sに加え、集合Vから外す
            list_S.append(sentence_num_tmp)
            list_V.remove(sentence_num_tmp)
            # 集合Sの累積単語数を更新する
            # word_num = sum([len(list_sentence_word[i]) for i in list_S])

        # list_Sをソート
        list_S_rev = sorted(list_S, key=lambda x: x)

        # list_S, list_sentence_S, list_sentence_Vのセット
        self.list_sentence_S = [list_sentence[i] for i in list_S_rev]
        self.list_S = list_S_rev
        self.list_sentence_V = list_sentence
