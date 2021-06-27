n = int(input())

res = cap = 0
for i in range(n):
    a, b = map(int, input().split())
    cap += (b - a)
    if cap < 0:
        cap = 0
    if cap > res:
        res = cap
print(res)
