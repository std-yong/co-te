import random

#2차원은 NxN 행렬로 구하기로 한다.
n = int(input("N 크기 입력: "))

def Make_2Arr(n): #랜덤값으로 채운 2차원배열 생성 함수
    dual_list = [[random.randint(1, 20) for _ in range(n)] for _ in range(n)]
    return dual_list
            

def Make_2psum(vv, n): #2차원 배열에 대한 구간합 생성 함수
    psum = [[0 for _ in range(n+1)] for _ in range(n+1)]
    for i in range(1, n+1):
        for j in range(1, n+1):
            psum[i][j] = vv[i-1][j-1] + (psum[i-1][j]) + (psum[i][j-1]) - (psum[i-1][j-1])
    return psum

vv = Make_2Arr(n) #랜덤 2차원배열 
psum = Make_2psum(vv, n) #구간합 

for row in vv: #랜덤 2차원배열 확인
    for col in row:
        print(col, end='\t')
    print()

print('\n') #구간합 확인
for row in psum:
    for col in row:
        print(col, end='\t')
    print()
    

def Part_Sum_2Arr(x1, y1, x2, y2, psum): #좌표에 대한 구간 합 구하는 공식
    S = psum[x2+1][y2+1] - psum[x1][y2+1] - psum[x2+1][y1] + psum[x1][y1]
    return S

x1, y1, x2, y2 = map(int, input("좌표 입력: ").split())

ppsum = Part_Sum_2Arr(x1,y1,x2,y2,psum)
print(ppsum) #결과 확인
    