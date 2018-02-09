# -*- coding: utf-8 -*-
# import ngram

sentence = "I am an NLPer"
words = sentence.split(' ')
for i in range(len(words)):
    print(''.join(words[i]) + ' ' , end ="")
    if(i+1 == len(words)):
        break
    else:
        print(''.join(words[i+1]))

# print(''.join(words[3]))
