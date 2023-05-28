import sys
input = sys.stdin.readline
n = int(input())

check_list = set()

for _ in range(n):
    name, status = input().split()

    if status == "enter":
        check_list.add(name)
    else:
        check_list.remove(name)

check_list = sorted(check_list, reverse=True)

for i in check_list:
    print(i)