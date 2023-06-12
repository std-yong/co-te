# math 라이브러리에 팩토리얼 함수가 있다
import math

result = []

T = int(input())

for _ in range(T):
    N, M = map(int, input().split())
    dari = math.factorial(M) // (math.factorial(N) * math.factorial(M - N))
    result.append(dari)

for i in result:
    print(i)