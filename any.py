# 1919 애너그램 만들기
word1 = list(input())
word2 = list(input())

last = []
for idx in word1:
    try:
        word2.remove(idx)
        last.append(idx)
    except:
        pass

for idx in last:
    word1.remove(idx)

print(len(word1 + word2))