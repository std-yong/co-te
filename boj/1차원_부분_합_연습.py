import random
#수열의 인덱스가 0부터 시작
def Make_Random_Sequence(n):  #크기가 n인 1차원 랜덤 리스트 생성
    v = [random.randint(1,20) for _ in range(n)] 
    return v

def Make_psum(v, n):  #수열의 누적 합으로 구성된 배열 생성
    psum = []
    hap = 0
    for i in range(n):
        hap += v[i]
        psum.append(hap)
    return psum

n = int(input("수열의 크기 입력: "))

v = Make_Random_Sequence(n)
psum = Make_psum(v, n)

print(v) #랜덤으로 구성한 수열
print(psum) #수열의 누적 합

i, j = map(int, input("원하는 구간 입력: ").split()) #1차원 부분 합

def Range_Sum(psum, i, j):
    if i == 0:
        rgs = psum[j]
    else: 
        rgs = psum[j] - psum[i-1]
    
    return rgs

print(Range_Sum(psum, i, j)) #수열의 부분 합 확인