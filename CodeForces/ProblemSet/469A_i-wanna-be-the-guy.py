n = int(input())
x = list(map(int, input().split()))
y = list(map(int, input().split()))
if len(set(x[1:] + y[1:])) == n:
    print('I become the guy.')
else:
    print('Oh, my keyboard!')
