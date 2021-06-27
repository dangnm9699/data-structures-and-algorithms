s = input()
t = input()
res = 'YES'
if len(s) != len(t):
    res = 'NO'
else:
    sl = len(s)
    for i in range(sl):
        if s[i] != t[sl - i - 1]:
            res = 'NO'
            break
print(res)
