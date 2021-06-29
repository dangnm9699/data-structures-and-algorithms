n = int(input())
a = list(map(int, input().split()))
res = 'EASY'
for i in a:
    if i == 1:
        res = 'HARD'
print(res)
