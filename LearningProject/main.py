import os

cwd = os.getcwd()
print(cwd)

# goal: open input.txt, store numbers in a tuple
# for every number convert it to its string
# build a map of number->string

result = []
with open('input.txt', 'r') as f:
    for line in f:
        result.append(int(line))
f.closed

print(result)

dict = {}

for num in result:
    dict[num] = str(num)

print(dict)

