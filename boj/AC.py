from collections import deque
result = []
T = int(input())
for _ in range(T):
    tk = True # 토큰으로 True일 때만 append
    func = input().strip() # 기능들 입력받음
    n = int(input()) # 횟수 입력 (필요가 있나?)
    que = deque(eval(input())) # 큐에 입력받는 값

    if len(func.replace('D', '')) % 2 == 0:
        print("짝")
    else:
        print('홀')
    
    for i in func:
        if que:
            if i == 'D':
                que.popleft()
            else:
                que.reverse()
        else:
            result.append('error')
            tk = False
    if tk:
        result.append(list(que))

for i in result:
    print(i)