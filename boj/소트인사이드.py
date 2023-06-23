n = input()
tmp = []
for i in n:
    tmp.append(i)

tmp.sort(reverse=True)

for j in tmp:
    print(j,end="")