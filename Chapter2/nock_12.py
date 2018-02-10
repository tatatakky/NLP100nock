# 各行の1列目だけを抜き出したものをcol1.txtに，2列目だけを抜き出したものをcol2.txtとしてファイルに保存せよ
# 確認にはcutコマンドを用いよ．
# cut -f 1 hightemp.txt (hightemp.txtの１列目を表示。)

#!usr/bin/env python
# -*- coding:utf-8 -*-

fout1=open('col1.txt','w')
fout2=open('col2.txt','w')
for line in open('hightemp.txt','r'):
    data=line.split()
    fout1.writelines(data[0]+'\n')
    fout2.writelines(data[1]+'\n')

fout1.close()
fout2.close()

# with open("hightemp.txt") as f1, open("col1.txt","w") as f2, open("col1.txt","w") as f3:
#     cols=list(zip(*[row.split("\t") for row in f1]))
#     f2.write("\n".join(cols[0]))
#     f3.write("\n".join(cols[1]))
