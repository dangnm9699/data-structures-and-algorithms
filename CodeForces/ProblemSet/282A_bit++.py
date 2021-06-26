n = int(input())
x = 0
for i in range(n):
    op = input()
    if op[1] == '+':
        x += 1
    else:
        x -= 1
print(x)
