import sys
input = sys.stdin.readline

N = int(input())
check = []

for i in range(N):
    check.append(input().rstrip())

check = list(set(check))
# set 자료형으로 중복을 제거 후 list로 만들어 정렬한다
check.sort() # 정렬
check.sort(key = len)

for i in check:
    print(i)    