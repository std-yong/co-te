import sys
input = sys.stdin.readline

def Binary_Search(jib):
    start, end = 1, jib[-1]-jib[0]
    result = 0
    while start <= end:
        mid = (start + end) // 2
        current = jib[0]
        count = 1
        
        for i in range(1, len(jib)):
            if jib[i] >= current + mid:
                current = jib[i]
                count += 1
        if count >= C:
            start = mid + 1
            result = mid
        else:
            end = mid- 1
            
    return result

N, C = map(int, input().split())
house = [int(input()) for _ in range(N)]
house.sort()
print(Binary_Search(house))