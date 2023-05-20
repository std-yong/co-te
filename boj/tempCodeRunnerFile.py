import sys, itertools
input = sys.stdin.readlines()

n = int(input())
data = list(map(int, input().split()))
permu = itertools.permutations(data, n) # 순열을 생성한다

# 차이가 최대인 값을 넣을 변수
cha_max = 0

for p in list(permu):
    # 차이의 합을 저장하는 임시 변수
    n_sum = 0

    # 차이의 합 계산
    for i in range(n-1):
        n_sum += abs(p[i]- p[i+1]) # 절대값

    # 차이의 합 최대값 비교
    if n_sum > cha_max:
        max = n_sum

print(max)

'''
순열 함수
import itertools
itertools.permutations(데이터가 들은 배열 리스트, 나열할 원소 갯수)

조합 함수
import itertools
itertools.combinations(데이터가 들은 배열 리스트, 나열할 원소 갯수)
'''