import sys
input = sys.stdin.readline
word, words = [], []
for _ in range(5):
    word = input()
    words.append(word)

result=""
for i in range(15):
    for j in range(5):
        if i < len(words[j]):
            result += words[j][i]

# 개행문자가 남아서 빼주는 작업
for i in result:
    if i == '\n':
        pass
    else:
        print(i,end='')