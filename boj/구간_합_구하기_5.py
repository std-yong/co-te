n, m = map(int, input().split())
vv = [list(map(int, input().split())) for _ in range(n)] #nxn 2차원 배열 생성 및 대입


psum = [[0 for _ in range(n+1)] for _ in range(n+1)]
for i in range(1, n+1):
    for j in range(1, n+1):
        psum[i][j] = vv[i-1][j-1] + (psum[i-1][j]) + (psum[i][j-1]) - (psum[i-1][j-1])

def Part_Sum_2Arr(x1, y1, x2, y2, psum): #좌표에 대한 구간 합 구하는 공식
    S = psum[x2+1][y2+1] - psum[x1][y2+1] - psum[x2+1][y1] + psum[x1][y1]
    return S

result = []

for m in range(m):
    x1, y1, x2, y2 = map(int, input().split())
    temp = Part_Sum_2Arr(x1-1,y1-1,x2-1,y2-1, psum)
    result.append(temp)

for i in range(len(result)):
    print(result[i])