s = input()

idx = 0
res = [False] * len('hello')
for i in range(len('hello')):
    for j in range(idx, len(s)):
        if 'hello'[i] == s[j]:
            res[i] = True
            idx = j + 1
            break

if all(res):
    print('YES')
else:
    print('NO')
