s1 = input().lower()
s2 = input().lower()
res = 0
for i in range(len(s1)):
    if s1[i] > s2[i]:
        res = 1
        break
    if s1[i] < s2[i]:
        res = -1
        break
print(res)
