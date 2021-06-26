x = y = 0
for i in range(5):
    m = list(map(int, input().split()))
    for j in range(5):
        if m[j] == 1:
            x = i - 2
            y = j - 2
            if x < 0:
                x *= -1
            if y < 0:
                y *= -1
print(x+y)
