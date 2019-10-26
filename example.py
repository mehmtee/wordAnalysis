import sys
from spliter import Splitter
text = open("text.txt", "r",encoding="utf8")

s = text.read()
c1 = Splitter(s)


c1.Analysis()


print(c1.punctuation)
print(c1.words) # kelime analizi
print(c1.conjunctionAnalysis()) #edat ve bağlaç
print(c1.sumLetters()) # toplam harf
print(c1.sumChar()) #toplam karakter
print(c1.sumWords()) #toplam harf

input("finish")
