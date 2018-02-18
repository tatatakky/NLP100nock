# Wikipedia記事のJSONファイルを読み込み，「イギリス」に関する記事本文を表示せよ．
# 問題21-29では，ここで抽出した記事本文に対して実行せよ．

# usr/bin/env python
#-*- coding:utf-8 -*-

import gzip,json
for line in gzip.open('jawiki-country.json.gz','rt'):
    country = json.loads(line)
    if country['title'] == 'イギリス':
        print(country['text'])
        break
