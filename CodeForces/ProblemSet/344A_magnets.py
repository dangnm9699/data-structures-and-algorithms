n = int(input())
stack = []
count = 0
for i in range(n):
    pos = int(input())
    if len(stack) == 0:
        stack.append(pos)
        count += 1
    else:
        if pos != stack[-1]:
            stack.pop()
            stack.append(pos)
            count += 1
print(count)
