n = int(input())
g = list(map(int, input().split()))
A = ['0']*n
for i in range(n):
    A[g[i] - 1] = str(i + 1)
print(' '.join(A))
