# 自然数Nをコマンドライン引数などの手段で受け取り，入力のファイルを行単位でN分割せよ
# 同様の処理をsplitコマンドで実現せよ
# split -l 9 hightemp.txt

# usr/bin/env python
#-*- coding:utf-8 -*-
import sys
def Judge_Remainder(divided,divisor):
    remainder=divided%divisor
    quotient=int(divided/divisor)
    if remainder is 0:
        return quotient
    else:
        return quotient+1
f=open('hightemp.txt')
N=int(sys.argv[1])
datas=[line for line in open('hightemp.txt')]
unity=Judge_Remainder(len(datas),N)
for i in range(unity):
    with open(str(i+1)+'.txt','w') as fout:
        fout.write("".join(datas[i*N:(i+1)*N]))
