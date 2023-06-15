def is_vps(s):
    stack = []
    for char in s:
        if char == '(':
            stack.append(char)
        elif char == ')':
            if not stack:
                return 'NO'
            stack.pop()
    return 'NO' if stack else 'YES'

result = []
N = int(input())
for _ in range(N):
    S = input()
    result.append(is_vps(S))

for i in result:
    print(i)


