import sys
input = sys.stdin.readline

N = int(input())
A1 = list(map(int, input().split()))
M = int(input())
A2 = list(map(int, input().split()))

A1.sort() # 처음 리스트 정렬한다

# 이분 탐색 함수
def binary_search(i):
    first = 0 # 처음 수
    end = N-1 # 마지막 수
    
    while first <= end:
        mid = (first + end) // 2
        if A1[mid] == i:
            return True
        
        if i < A1[mid]: # i가 mid 보다 작을 때
            end = mid-1
            
        elif i > A1[mid]: # i가 mid 보다 클 때
            first = mid+1
            
for i in range(M):
    if binary_search(A2[i]):
        print(1)
    else:
        print(0)