import sys
from collections import deque
input = sys.stdin.readline

que = deque()
result = []
N = int(input())

# 입력이 두번일 때를 어떻게 처리할지 몰라서 좀 찾아봐서 알게되었다.
for _ in range(N):
    cmd = input().split() # 입력 받음
    if cmd[0] == "push": # push일 때
        que.append(int(cmd[1]))
        
    elif cmd[0] == "pop": # pop일 때
        if que: # 큐가 비어있는지 확인
            result.append(que.popleft())
        else:
            result.append(-1)
            
    elif cmd[0] == "size": # size일 때
        result.append(len(que))
        
    elif cmd[0] == "empty": # empty일 때
        if que:
            result.append(0)
        else:
            result.append(1)
            
    elif cmd[0] == "front": # front일 때
        if que:
            result.append(que[0])
        else:
            result.append(-1)
            
    elif cmd[0] == "back": # back일 때
        if que:
            result.append(que[-1])
        else:
            result.append(-1)

for i in result:
    print(i)