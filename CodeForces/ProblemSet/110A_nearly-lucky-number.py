n = int(input())
nl = 'YES'
count = 0
while n > 0:
    digit = n % 10
    if digit == 4 or digit == 7:
        count += 1
    n //= 10
if count != 4 and count != 7:
    nl = 'NO'
print(nl)
