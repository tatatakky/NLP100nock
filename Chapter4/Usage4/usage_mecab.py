import MeCab
string = "吾輩は猫である。"
mecab = MeCab.Tagger()
print(mecab.parse(string),end="")
