# 12で作ったcol1.txtとcol2.txtを結合し，元のファイルの1列目と2列目をタブ区切りで並べたテキストファイルを作成せよ
# 確認にはpasteコマンドを用いよ．
# paste col1.txt col2.txt

#!usr/bin/env python
# -*- coding:utf-8 -*-

with open('col1.txt') as f1, open('col2.txt') as f2, open('col3.txt','w') as fout:
    li = [c1.replace('\n','') + '\t' + c2 for c1,c2 in zip(f1,f2)]
    fout.write("".join(li))
