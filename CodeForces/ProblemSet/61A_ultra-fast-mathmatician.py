s1 = input()
s2 = input()
le = len(s1)
res = ''
for i in range(le):
    res += str(int(s1[i] != s2[i]))
print(res)
