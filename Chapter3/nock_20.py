# Wikipedia記事のJSONファイルを読み込み，「イギリス」に関する記事本文を表示せよ．
# 問題21-29では，ここで抽出した記事本文に対して実行せよ．

# usr/bin/env python
#-*- coding:utf-8 -*-
from extraction_country import Extraction
print(Extraction("イギリス"))
