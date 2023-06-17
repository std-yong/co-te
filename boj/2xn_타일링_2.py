N = int(input())
arr = [0] * 1001
arr = [1, 1] # 명확한 값이기에 미리 선언

for i in range(2, N+1):
    arr.append(arr[i-1] + ((arr[i-2] * 2))) # 점화식 이용
    
print(arr[N] % 10007)