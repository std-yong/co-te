import sys
input = sys.stdin.readline

nanjang_e = [int(input()) for _ in range(9)]
nanjang_e.sort()

hap = sum(nanjang_e)
cha = hap - 100
removed = False  # 이미 제거한 경우를 체크하기 위한 변수

for i in range(len(nanjang_e)):
    if removed:
        break
    tmp = cha - nanjang_e[i]
    for j in range(i+1, len(nanjang_e)):
        if nanjang_e[j] == tmp:
            nanjang_e.pop(j)  # 인덱스 j의 요소 제거
            nanjang_e.pop(i)  # 인덱스 i의 요소 제거
            removed = True  # 요소 제거를 표시
            break

for i in range(len(nanjang_e)):
    print(nanjang_e[i])
