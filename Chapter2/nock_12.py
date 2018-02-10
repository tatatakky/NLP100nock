# 各行の1列目だけを抜き出したものをcol1.txtに，2列目だけを抜き出したものをcol2.txtとしてファイルに保存せよ
# 確認にはcutコマンドを用いよ．
fout1=open('col1.txt','w')
fout2=open('col2.txt','w')
for line in open('hightemp.txt','r'):
    data=line.split()
    fout1.writelines(data[0]+'\n')
    fout2.writelines(data[1]+'\n')

fout1.close()
fout2.close()
