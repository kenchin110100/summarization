# coding: utf-8
"""
numpyでは操作できないベクトルの計算を行うクラス
"""
import numpy as np
from scipy import spatial
from sklearn.cluster import KMeans


class Vector:

    # ベクトルリストの類似度行列を作成
    @classmethod
    def cal_similarity_matrix(cls, list_vector):
        # 作成する行列の行数を確認
        num_row = len(list_vector)
        # 最終的に出力する類似度行列
        arr_similarity = np.zeros((num_row, num_row))
        # cos類似度を計算
        for i in range(num_row):
            for j in range(i, num_row):
                similarity = 1.0 - spatial.distance.cosine(list_vector[i],
                                                           list_vector[j])
                arr_similarity[i][j] = similarity
                arr_similarity[j][i] = similarity

        return arr_similarity

    # ベクトルリストをkmeansクラスタリング
    @classmethod
    def cal_clustering(cls, list_vector, K, random_state=3):
        # sklearnのインスタンス化
        kmeans = KMeans(n_clusters=K, random_state=random_state)
        # クラスタリング
        kmeans_model = kmeans.fit(list_vector)
        # ラベルのリストを返す
        list_labels = kmeans_model.labels_

        return list_labels

    # ベクトルリスト間の非類似度行列を作成
    @classmethod
    def cal_mutual_similarity_matrix_inv(cls, list_vector1, list_vector2):
        # 作成する行列の行数と列数を確認
        num_row = len(list_vector1)
        num_col = len(list_vector2)
        # 最終的に出力する類似度行列
        arr_similarity_inv = np.zeros((num_row, num_col))
        # cos類似度を計算
        for i in range(num_row):
            for j in range(num_col):
                similarity = spatial.distance.cosine(list_vector1[i], list_vector2[j])
                arr_similarity_inv[i][j] = similarity

        return arr_similarity_inv
