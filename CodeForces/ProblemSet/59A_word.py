s = input()
print([s.lower(), s.upper()][sum(x <= 'Z' for x in s) * 2 > len(s)])
