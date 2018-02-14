# 1列目の文字列の種類（異なる文字列の集合）を求めよ．
# 確認にはsort, uniqコマンドを用いよ．
# cut -f 1 hightemp.txt | sort | uniq

# usr/bin/env python
#-*- coding:utf-8 -*-

with open('hightemp.txt','r') as f:
    prefecture=set([lines.split('\t')[0] for lines in f])
    print(prefecture)
