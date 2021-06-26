vowels = ['A', 'O', 'Y', 'E', 'U', 'I', 'a', 'o', 'y', 'u', 'e', 'i']

string = input()
result = [""]
for i in range(len(string)):
    if string[i] not in vowels:
        result.append(string[i].lower())
print(".".join(result))
