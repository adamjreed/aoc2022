import re

input = open('input.txt', 'r')
assignments = []

for line in input:
    assignments.append([(int(pair[0]), int(pair[1])) for pair in re.findall("(\d+)-(\d+)", line.strip())])

def contains(pair):
    return pair[0][0] <= pair[1][0] and pair[0][1] >= pair[1][1] \
        or pair[1][0] <= pair[0][0] and pair[1][1] >= pair[0][1]

def overlaps(pair):
    return pair[1][0] <= pair[0][0] <= pair[1][1] or pair[1][0] <= pair[0][1] <= pair[1][1] \
        or pair[0][0] <= pair[1][0] <= pair[0][1] or pair[0][0] <= pair[1][1] <= pair[0][1]

def part1(assignments):
    return len(list(filter(contains, assignments)))

def part2(assignments):
    return len(list(filter(overlaps, assignments)))

print(f'part 1: %d' % part1(assignments))
print(f'part 2: %d' % part2(assignments))