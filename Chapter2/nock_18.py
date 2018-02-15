# 各行を3コラム目の数値の逆順で整列せよ（注意: 各行の内容は変更せずに並び替えよ)
# 確認にはsortコマンドを用いよ（この問題はコマンドで実行した時の結果と合わなくてもよい)

# usr/bin/env python
#-*- coding:utf-8 -*-

temperature=[line.split('\t')[2] for line in open('hightemp.txt','r')]
datas=[line for line in open('hightemp.txt','r')]
dictionary=dict(zip(datas,temperature))
sort = sorted(dictionary.items(),key=lambda x:x[1])
for data,temp in sort:
    print(data,end="")

# lambda 引数:処理内容
