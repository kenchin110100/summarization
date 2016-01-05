# coding: utf-8
"""
ファイルを作成するためのクラス
"""
import csv
import pickle
import os, sys


# csvファイルを作成するためのクラス
class Filer:
    # csvファイルをそのまま読み込み2次配列に格納
    @classmethod
    def readcsv(cls, filepath):
        f = open(filepath, 'rb')
        csvReader = csv.reader(f)
        arr = [row for row in csvReader]
        f.close()
        return arr

    # 2次配列をcsvファイルに書き込む
    @classmethod
    def writecsv(cls, arr, filepath):
        f = open(filepath, 'ab')
        csvWriter = csv.writer(f)
        for row in arr:
            csvWriter.writerow(row)
        f.close()

    # logfileを作成
    @classmethod
    def writelog(cls, string, filepath):
        f = open(filepath, 'ab')
        f.write(string)
        f.close()

    # unicodeの2次元配列をutf8に変換してからcsvファイルに書き込み
    @classmethod
    def writecsv_unicode(cls, arr, filepath):
        arr = [[elem.encode('utf-8') for elem in row] for row in arr]
        cls.writecsv(arr, filepath)

    # pickleを使った読み込み
    @classmethod
    def readpickle(cls, path):
        f = open(path)
        l = pickle.load(f)
        f.close()
        return l

    # 文字コードの判定
    @classmethod
    def guess_charset(cls, data):
        f = lambda d, enc: d.decode(enc) and enc

        try: return f(data, 'utf-8')
        except: pass
        try: return f(data, 'shift-jis')
        except: pass
        try: return f(data, 'euc-jp')
        except: pass
        try: return f(data, 'iso2022-jp')
        except: pass
        return None

    # utf-8に文字コードを変換
    @classmethod
    def conv(cls, data):
        charset = cls.guess_charset(data)
        if charset is None:
            u = data
        else:
            u = data.decode(charset)
        return u.encode('utf-8')

