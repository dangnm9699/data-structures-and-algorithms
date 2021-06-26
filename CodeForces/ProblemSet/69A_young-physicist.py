n = int(input())

x = y = z = 0
for i in range(n):
    xi, yi, zi = map(int, input().split())
    x += xi
    y += yi
    z += zi
if x != 0 or y != 0 or z != 0:
    print("NO")
else:
    print("YES")
