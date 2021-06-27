input()
r = input()
res = 0
for c in r:
    if c == 'A':
        res += 1
    if c == 'D':
        res -= 1
if res == 0:
    print('Friendship')
elif res > 0:
    print('Anton')
else:
    print('Danik')
