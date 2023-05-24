import sys
input = sys.stdin.readline

answer = 0

square = [[0 for _ in range(100)] for _ in range(100)]
n = int(input())

for i in range(n):
    width, length = map(int, input().split())
    for i in range(width, width+10):
        for j in range(length, length+10):
            square[i][j] = 1


for i in square:
    for j in i:
        if j == 1:
            answer+=1
# 이 부분을 보니까 이렇게도 하더라
'''
for i in square:
    answer += i.count(1)
'''
print(answer)