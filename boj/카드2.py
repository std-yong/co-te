import sys
input = sys.stdin.readline

from collections import deque

N = int(input())
queue = deque() #큐 생성

for i in range(N):
    queue.append(i+1) #큐에 순차적으로 삽입
    
while len(queue) > 1:
    queue.popleft() #왼쪽거 빼고
    queue.append(queue.popleft()) #한번 더 뺀걸 오른쪽에 삽입
    
print(queue.pop())
