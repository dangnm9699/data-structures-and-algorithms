n = int(input())
p = list(map(int, input().split()))
r = 0
for i in range(n):
    r += p[i]
print(r / n)
