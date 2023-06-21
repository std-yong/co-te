def solution(a, b, n):
    total = 0
    while n >= a:
        q, r = divmod(n, a)   # n을 a로 나눈 몫과 나머지
        total += q * b        # 몫 만큼 콜라를 받을 수 있음
        n = r + q * b         # 현재 가지고 있는 빈 병의 개수
    return total
