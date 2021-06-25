n = int(input())
s = input()
count = current = 0
for i in s:
    if current == i:
        count += 1
    current = i
print(count)
