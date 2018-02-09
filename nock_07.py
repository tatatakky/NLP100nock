# 引数x, y, zを受け取り「x時のyはz」という文字列を返す関数を実装せよ．さらに，x=12, y="気温", z=22.4として，実行結果を確認せよ．

#!/usr/bin/env python
# -*- coding: utf-8 -*-

def CharString(time,temp,degree):
    return  "{}時の{}は{}".format(time,temp,degree)
x=12
y="気温"
z=22.4
print(CharString(x,y,z))
