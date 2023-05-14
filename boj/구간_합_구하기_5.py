# 입력을 받습니다.
n, m = map(int, input().split())
matrix = [list(map(int, input().split())) for _ in range(n)]

# 부분합을 계산합니다.
sum_matrix = [[0] * (n+1) for _ in range(n+1)]  # 부분합 행렬을 저장할 리스트
for i in range(1, n+1):
    for j in range(1, n+1):
        sum_matrix[i][j] = matrix[i-1][j-1] + sum_matrix[i-1][j] + sum_matrix[i][j-1] - sum_matrix[i-1][j-1]

temp = []
# 쿼리에 대한 결과를 출력합니다.
for _ in range(m):
    x1, y1, x2, y2 = map(int, input().split())
    result = sum_matrix[x2][y2] - sum_matrix[x2][y1-1] - sum_matrix[x1-1][y2] + sum_matrix[x1-1][y1-1]
    temp.append(result)
    
for _ in range(m):
    print(temp[i])