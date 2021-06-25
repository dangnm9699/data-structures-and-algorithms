s = input()
count = current = 1
res = "NO"
for i in s:
    if current == i:
        count += 1
    else:
        count = 1
    if count == 7:
        res = "YES"
        break
    current = i

print(res)
