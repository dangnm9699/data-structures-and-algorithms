n = int(input())
r = list(map(int, input().split()))
max_idx = min_idx = 0
for i in range(n):
    if r[i] <= r[min_idx]:
        min_idx = i
    if r[i] > r[max_idx]:
        max_idx = i
if max_idx < min_idx:
    print(max_idx + n - 1 - min_idx)
else:
    print(max_idx + n - 2 - min_idx)
