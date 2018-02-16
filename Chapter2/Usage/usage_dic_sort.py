# usr/bin/env python
#-*- coding:utf-8 -*-

key=['2','1','3','4','5']
value=['bb','aa','cc','dd','ee']
dic=dict(zip(key,value))
# sorted(ディクショナリの中身一覧, key=lambda x:ソートしたい部分)
sort_data = sorted(dic.items(),key=lambda x:x[1])
print(sort_data)
