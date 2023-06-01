from collections import deque
result = []

testcase = int(input())

for _ in range(testcase):
    N, M = map(int, input().split()) # N, M 입력받음
    que = deque(map(int, input().split())) # 입력받아 큐 생성
    index = deque(range(0, N)) # index를 셀 큐 생성
    cnt = 0 # 몇번째인지 세려고 카운트 변수 생성
    
    while que: # 큐에 대한 탐색 시작
        if que[0] == max(que): # 처음부터 최대값인지 확인
            cnt += 1 # 우선 하나 늘리고 
            que.popleft() # 뺀다
            if index.popleft() == M: # 만약 찾는값이라면
                result.append(cnt) # 결과에 저장
        else: # 이제 처음이 아닐경우에 실행함
            que.append(que.popleft()) 
            index.append(index.popleft())
            
# deque에도 sort가 있다면 좀 더 편하게 풀지 않았을까?
for i in result:
    print(i)