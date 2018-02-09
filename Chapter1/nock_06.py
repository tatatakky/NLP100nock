# "paraparaparadise"と"paragraph"に含まれる文字bi-gramの集合を，それぞれ, XとYとして求め，XとYの和集合，積集合，差集合を求めよ．
# さらに，'se'というbi-gramがXおよびYに含まれるかどうかを調べよ

#!/usr/bin/env python
# -*- coding: utf-8 -*-

str1="paraparaparadise"
str2="paragraph"
def ngram(CharStr, n):
    List = []
    for i in range(n-1,len(CharStr)+1):
        List.append(CharStr[i-n:i])
    List.remove('')
    return List

# ngram の list を set に; 重複を排除できる上に集合演算が出来る
X = set(ngram(str1, 2))
Y = set(ngram(str2, 2))

print("X + Y = {}".format(X.union(Y)))
print("X * Y = {}".format(X.intersection(Y)))
print("X - Y = {}".format(X.difference(Y)))

print('se' in X)
print('se' in Y)
