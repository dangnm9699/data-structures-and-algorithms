n = int(input())
res = []
for i in range(n):
    if i % 2 == 0:
        res.append('I hate')
    else:
        res.append('I love')
print(' that '.join(res) + ' it')
