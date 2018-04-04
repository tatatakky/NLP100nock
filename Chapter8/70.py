pos_list=[]
with open('./rt-polaritydata/rt-polaritydata/rt-polarity.pos') as sentiment:
    for line in sentiment:
        pos_list.append(str("+1 "+line))

neg_list=[]
with open('./rt-polaritydata/rt-polaritydata/rt-polarity.neg') as sentiment:
    for line in sentiment:
        neg_list.append(str("-1 "+line))

concatenat = pos_list + neg_list

pos_num=0
neg_num=0
