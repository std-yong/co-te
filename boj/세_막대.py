import sys
input = sys.stdin.readline

a,b,c = map(int, input().split())
long = max(a,b,c)
short = sum((a,b,c)) - long

while short <= long:
    long -= 1

print(long + short)