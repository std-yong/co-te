import sys
input = sys.stdin.readline

N, M = map(int, input().split())
 
pokemon = dict() # 포켓몬 이름에 대한 번호 딕셔너리
pokemon_number = dict() # 포켓몬 번호에 대한 이름 딕셔너리
questions = list() # 질문 리스트

for i in range(1, N+1):
    name = input().rstrip()
    pokemon[name] = i
    pokemon_number[i] = name

for _ in range(M):
    tmp = input().rstrip()
    questions.append(tmp)

for i in questions:
    if i.isdigit(): # 질문이 숫자인 경우
        print(pokemon_number[int(i)])
    else: # 질문이 이름인 경우
        print(pokemon[i])