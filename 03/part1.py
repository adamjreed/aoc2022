input = open('input.txt', 'r')
lines = input.readlines()

def priority(char):
    i = ord(char)

    if i > 90:
        return i - 96

    return i - 38

priority_sum = 0

for line in lines:
    chars = list(line.strip())

    first_half = chars[:len(chars)//2]
    second_half = chars[len(chars)//2:]

    intersection = set(first_half).intersection(second_half)

    priority_sum += priority(list(intersection)[0])

print(priority_sum)