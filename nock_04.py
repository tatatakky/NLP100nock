#-*- coding: utf-8 -*-
sentence = 'Hi He Lied Because Boron Could Not Oxidize Fluorine. New Nations Might Also Sign Peace Security Clause. Arthur King Can.'
sentence_change = sentence.replace('.','')
each_word = sentence_change.split(' ')
dictionary = {}
for i in range(len(each_word)):
    if(i==0 or i==4 or i==5 or i==6 or i==7 or i==8 or i==14 or i==15 or i==18):
        dictionary[i+1] = each_word[i][0]
    else:
        dictionary[i+1] = each_word[i][0:2]

print(dictionary)
