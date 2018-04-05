"""
文に関する極性分析の正解データを用い，以下の要領で正解データ（sentiment.txt）を作成せよ．

rt-polarity.posの各行の先頭に"+1 "という文字列を追加する（極性ラベル"+1"とスペースに続けて肯定的な文の内容が続く）
rt-polarity.negの各行の先頭に"-1 "という文字列を追加する（極性ラベル"-1"とスペースに続けて否定的な文の内容が続く）
上述1と2の内容を結合（concatenate）し，行をランダムに並び替える
sentiment.txtを作成したら，正例（肯定的な文）の数と負例（否定的な文）の数を確認せよ
"""

# usr/bin/env python
# -*- coding:utf-8 -*-
import random,codecs

with codecs.open('./rt-polaritydata/rt-polarity.pos',encoding='utf-8',errors='ignore') as sentiment:
    pos_list = ["+1 " + line for line in sentiment]

with open('./rt-polaritydata/rt-polarity.neg',encoding='utf-8',errors='ignore') as sentiment:
    neg_list = ["-1 " + line for line in sentiment]

concatenat = pos_list + neg_list

print("pos:{},neg:{}".format(len(pos_list),len(neg_list)))

# random.shuffle(concatenat)
# print(concatenat[:10])
