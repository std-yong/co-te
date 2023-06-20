from itertools import combinations

def is_prime(n):
    if n < 2:
        return False
    if n == 2 or n == 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True

def solution(nums):
    answer = 0
    for comb in combinations(nums, 3):
        if is_prime(sum(comb)):
            answer += 1
    return answer
