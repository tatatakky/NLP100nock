# 自然数Nをコマンドライン引数などの手段で受け取り，入力のうち末尾のN行だけを表示せよ
# 確認にはtailコマンドを用いよ．

#!usr/bin/env python
# -*- coding:utf-8 -*-
import sys
assert len(sys.argv) is 2,"[usage]: python nock_14.py N"
lines = [line for line in open("hightemp.txt","r")]
print(''.join(lines[-int(sys.argv[1]):]),end="")

# with open("hightemp.txt") as f:
#     print("".join(f.readlines()[-int(sys.argv[1]):]), end="")
