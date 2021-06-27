n, h = map(int, input().split())
res = 0
for i in list(map(int, input().split())):
    res += 1
    if i > h:
        res += 1
print(res)