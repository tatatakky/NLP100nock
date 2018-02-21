import re
pattern = r"^\[Chopin:(.*?)\]"
text = "[Chopin:Noctorne]"
match = re.search(pattern , text)
print(match.group(1)) # マッチした文字列を返す
