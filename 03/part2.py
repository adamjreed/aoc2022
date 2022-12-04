input = open('input.txt', 'r')
lines = input.readlines()

def priority(char):
    i = ord(char)

    if i > 90:
        return i - 96

    return i - 38

priority_sum = 0
group = []

for line in lines:
    group.append(list(line.strip()))
    if len(group) < 3:
        continue

    intersection = set(group[0]).intersection(group[1]).intersection(group[2])

    priority_sum += priority(list(intersection)[0])

    group = []

print(priority_sum)