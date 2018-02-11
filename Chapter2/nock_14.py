# 自然数Nをコマンドライン引数などの手段で受け取り，入力のうち先頭のN行だけを表示せよ．
# 確認にはheadコマンドを用いよ．
# head -n 5 hightemp.txt

# !usr/bin/env python
# -*- coding;utf-8 -*-
import sys
N = int(sys.argv[1])
assert len(sys.argv) is 2, "usage: python nock_14.py [N]"
with open('hightemp.txt') as f:
    print(''.join(f.readlines()[:N]),end="")

    # count=0
    # for line in f.readlines() :
    #     if count is N:
    #         break
    #     else:
    #         print(line,end="")
    #     count+=1
