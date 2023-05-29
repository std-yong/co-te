import sys
from collections import Counter
input = sys.stdin.readline

N = int(input())
first = list(map(int, input().split()))

M = int(input())
second = list(map(int, input().split()))

counter = Counter(first) # first 리스트에 대한 카운터 저장
# Counter의 key는 요소를 기준으로 갯수를 value에 저장함
result = []
for i in second:
    result.append(counter[i])

print(*result) # *붙혀서 리스트 값만 출력