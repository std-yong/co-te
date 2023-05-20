import sys, itertools
input = sys.stdin.readline

N = int(input())
data = list(map(int, input().split()))

# 순열 생성
permu = itertools.permutations(data, N)

# 차이가 최대인 값을 넣을 변수
cha_Max = 0

for p in list(permu):
    n_Sum = 0    # 차이의 합을 저장하는 임시 변수

    for i in range(N-1):     # 차이의 합을 저장하는 임시 변수
        n_Sum += abs(p[i]- p[i+1])

    if n_Sum > cha_Max:    # 차이의 합을 저장하는 임시 변수
        cha_Max = n_Sum

print(cha_Max)

'''
순열 함수
import itertools
itertools.permutations(데이터가 들은 배열 리스트, 나열할 원소 갯수)

조합 함수
import itertools
itertools.combinations(데이터가 들은 배열 리스트, 나열할 원소 갯수)
'''