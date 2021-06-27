y = int(input())
while True:
    y += 1
    a = set(str(y))
    if len(a) == 4:
        print(y)
        break
