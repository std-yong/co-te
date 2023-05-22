import sys
input = sys.stdin.readline

N, M = map(int, input().split())
A, B = [], []

# 입력 받기
for _ in range(N):
    tmp = list(map(int, input().split()))
    A.append(tmp)
    
for _ in range(N):
    tmp2 = list(map(int, input().split()))
    B.append(tmp2)

# 덧셈
for i in range(N):
    for j in range(M):
        print(A[i][j] + B[i][j], end=' ')
    print()
