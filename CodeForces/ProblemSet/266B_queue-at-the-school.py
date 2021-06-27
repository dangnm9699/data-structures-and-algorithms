n, t = map(int, input().split())
s = list(input())

for i in range(t):
    swaps = []
    idx = 0
    swapped = False
    while idx < len(s) - 1:
        if s[idx] == 'B' and s[idx + 1] == 'G':
            swaps.append([idx, idx + 1])
            swapped = True
            idx += 1
        idx += 1
    if not swapped:
        break
    for swap in swaps:
        s[swap[0]], s[swap[1]] = s[swap[1]], s[swap[0]]
print(''.join(s))
