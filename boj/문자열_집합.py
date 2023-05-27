def string_set(N,M):
    cnt = 0
    for i in N:
        for j in M:
            if i == j:
                cnt += 1
    return cnt

n, m = map(int, input().split())
N = list(input() for _ in range(n))
M = list(input() for _ in range(m))

print(string_set(N,M))