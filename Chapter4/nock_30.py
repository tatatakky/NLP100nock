# 形態素解析結果（neko.txt.mecab）を読み込むプログラムを実装せよ．
# ただし，各形態素は表層形（surface），基本形（base），品詞（pos），品詞細分類1（pos1）をキーとするマッピング型に格納し，1文を形態素（マッピング型）のリストとして表現せよ．
# 第4章の残りの問題では，ここで作ったプログラムを活用せよ

# usr/bin/env python
# -*- coding:utf-8 -*-
import MeCab

def parse():
    with open('neko.txt','r') as fdata, open('neko.txt.mecab','w') as output:
        mecab=MeCab.Tagger()
        readfile=fdata.read()
        output.write(mecab.parse(readfile))

def MappingLines():
    

parse()
