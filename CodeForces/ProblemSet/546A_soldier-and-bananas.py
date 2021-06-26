k, n, w = map(int, input().split())
borrow = 0
for i in range(w):
    borrow += (i + 1) * k
if borrow < n:
    print(0)
else:
    print(borrow - n)
