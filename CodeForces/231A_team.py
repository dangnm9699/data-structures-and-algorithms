n = int(input())

count = 0

for i in range(n):
    p, v, t = map(int, input().split())
    if (p == 1 and v == 1) or (p == 1 and t == 1) or (v == 1 and t == 1):
        count += 1

print(count)