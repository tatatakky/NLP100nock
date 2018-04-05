"""
英語のストップワードのリスト（ストップリスト）を適当に作成せよ．
さらに，引数に与えられた単語（文字列）がストップリストに含まれている場合は真，それ以外は偽を返す関数を実装せよ．
さらに，その関数に対するテストを記述せよ．
"""
# udr/bin/env python
# -*- coding:utf-8 -*-
from nltk.corpus import stopwords
stopwords_list = [s for s in stopwords.words('english')]
# print(stopwords_list)
def check_is_stopword(word):
    if word in stopwords_list:
        return True
    else:
        return False

print(check_is_stopword("we"))
