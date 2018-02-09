# 与えられた文字列の各文字を，以下の仕様で変換する関数cipherを実装せよ．
#
# 英小文字ならば(219 - 文字コード)の文字に置換
# その他の文字はそのまま出力
# この関数を用い，英語のメッセージを暗号化・復号化せよ．

#!usr/bin/env python
# -*- coding:utf-8 -*-

def cipher(string):
    cipher_str=""
    for char in string:
        if char.islower() is True:
            cipher_str += chr(219-ord(char))
        else:
            cipher_str += char
    return cipher_str

charstring="Natural Language Processing"
print(cipher(charstring))
print(cipher(cipher(charstring)))

# ordで文字コードに変換
# chrで文字に変換
