x = int(input())
step = 0
for i in range(5, 0, -1):
    if x == 0:
        break
    step += (x // i)
    x %= i
print(step)
