# coding: utf-8
"""
文書間の違いを計算するためのメインクラス
"""
import numpy as np
import ConfigParser
import sys
from functions.filer import Filer
from functions.sentence import Sentence
from functions.vector import Vector


class Summarization2:
    def __init__(self, K, gamma, epsilon, lamda):
        # ガンマの値
        self.gamma = gamma
        # ラムダの値
        self.lamda = lamda
        # イプシロンの値
        self.epsilon = epsilon
        # クラスタ数
        self.K = K
        # list_S
        self.list_S = None
        # 要約文
        self.list_sentence_S = None

        # configファイルの読み込み
        try:
            inifile = ConfigParser.ConfigParser()
            inifile.read('/var/www/cgi-bin/test_proj/summarization/files/config.ini')
            # 分散表現を記録したdictのパス
            self.dictpath = inifile.get('Dictionary', 'dictpath')
            self.neologdpath = inifile.get('Dictionary', 'neologdpath')

        except IOError:
            print 'Can not find config.ini'
            sys.exit()

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
    def _cal_f_doc(self, list_sentence_num,
                   arr_similarity, arr_similarity_inv,
                   arr_C_V1, arr_C_V2, list_sentence_labels,
                   gamma, epsilon, lamda):
        L_S_in = self._cal_L_S(list_sentence_num, arr_similarity, gamma, arr_C_V1)
        L_S_out = self._cal_L_S(list_sentence_num, arr_similarity_inv, epsilon, arr_C_V2)
        R_S = self._cal_R_S(list_sentence_num, list_sentence_labels)
        f_doc = L_S_in + epsilon * L_S_out + lamda * R_S

        return f_doc

    def cal_greedy(self, sentence1, sentence2, limit_sentence_num):
        # 要約文の累積単語数
        # word_num = 0
        # sentence1のリスト化
        list_sentence1 = self.sentence.separate_sentence(sentence1)
        # sentence2のリスト化
        list_sentence2 = self.sentence.separate_sentence(sentence2)
        # 要約文のラベル集合
        list_S = []
        # 文書集合のラベル集合
        list_V = [i for i in range(len(list_sentence1))]

        # 文を分かち書きする
        list_sentence1_word = [self.sentence.sentence_owakati(sentence)
                               for sentence in list_sentence1]
        # 文を分かち書きする
        list_sentence2_word = [self.sentence.sentence_owakati(sentence)
                               for sentence in list_sentence2]
        # リストの文章をベクトルに置き換える
        dict_word_to_vector = Filer.readpickle(self.dictpath)
        list_sentence1_vector = [self.sentence.sentence_to_vector(sentence_word,
                                                                  dict_word_to_vector)
                                for sentence_word in list_sentence1_word]
        list_sentence2_vector = [self.sentence.sentence_to_vector(sentence_word,
                                                                  dict_word_to_vector)
                                for sentence_word in list_sentence2_word]
        # 文間の類似度を計算
        arr_similarity = Vector.cal_similarity_matrix(list_sentence1_vector)
        # 文書間の類似度を計算
        arr_similarity_inv = Vector.cal_mutual_similarity_matrix_inv(list_sentence2_vector, list_sentence1_vector)
        # C_V1を計算
        arr_C_V1 = self._cal_C_V(arr_similarity)
        arr_C_V2 = self._cal_C_V(arr_similarity_inv)
        # 文書をクラスタリング
        list_sentence_labels = Vector.cal_clustering(list_sentence1_vector,
                                                     self.K)

        # 劣モジュラ関数の修正貪欲法
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
                                        arr_similarity_inv,
                                        arr_C_V1,
                                        arr_C_V2,
                                        list_sentence_labels,
                                        self.gamma,
                                        self.epsilon,
                                        self.lamda)
                # 計算後に文iを集合Sから除く
                list_S.pop()
                # f_doc / c がその時点の最高スコアなら記録
                if f_doc > score_tmp:
                    score_tmp = f_doc
                    sentence_num_tmp = i

            # 最高スコアを記録した文iを集合Sに加え、集合Vから外す
            list_S.append(sentence_num_tmp)
            list_V.remove(sentence_num_tmp)

        # list_Sをソート
        list_S_rev = sorted(list_S, key=lambda x: x)

        # list_S, list_sentence_Sのセット
        self.list_sentence_S = [list_sentence1[i] for i in list_S_rev]
        self.list_S = list_S
        self.list_sentence_V = list_sentence1
