n = int(input())
res = False
for i in [4, 7, 47, 74, 447, 474, 477, 747, 774]:
    if n % i == 0:
        res = True
        break
if res:
    print('YES')
else:
    print('NO')
