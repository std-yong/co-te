from collections import deque
N, M = map(int, input().split()) # M은 왜 입력받는거여.. ㅋㅋ
answer = list(map(int, input().split())) # 두번째줄 입력값으로 리스트 생성
que = deque(i for i in range(1, N+1)) # 1~N+1의 범위로 숫자 생성
cnt = 0 # 카운트 담을 변수 초기화

for i in answer: # 찾을 값으로 루프 진행
    while que: # 큐를 진행하며
        if que[0] == i: # 맨 앞 값이 일치하면
            que.popleft() # 큐에서 빼내고
            break # while루프 탈출
        else: # 값이 일치하지 않을 시에는
            if que.index(i) < len(que)/2: # 왼쪽 or 오른쪽 어디로 돌지 정하기
                # que의 index는 현재 i의 위치를 반환함, 큐의 절반보다 적을 때 왼쪽 길면 오른쪽
                while que[0] != i:
                    que.append(que.popleft()) # 왼쪽에서 뺀 값 오른쪽 끝으로
                    cnt += 1
            else:
                while que[0] != i:
                    que.appendleft(que.pop()) # 오른쪽에서 뺀 값 왼쪽 끝으로
                    cnt += 1
                    
print(cnt) # 돈 횟수 출력