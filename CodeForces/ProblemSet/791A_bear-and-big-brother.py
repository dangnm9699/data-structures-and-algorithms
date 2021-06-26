a, b = map(int, input().split())
year = 0
while True:
    if a > b:
        break
    year += 1
    a *= 3
    b *= 2
print(year)
