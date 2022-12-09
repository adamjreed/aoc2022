input = open('input.txt', 'r')
def calc_sizes(dir, sizes):
    size = 0

    for sub in dir["dirs"].values():
        size += calc_sizes(sub, sizes)

    for file in dir["files"].values():
        size += int(file)

    sizes.append(size)

    return size

root = {"dirs": {}, "files": {}}
pointer = root
pwd = []

for line in input:
    if line.strip() == "$ cd /":
        continue

    if line[0] == "$":
        parts = line.strip().split(" ")
        if parts[1] == "cd":
            if parts[2] == "..":
                pwd.pop()
            else:
                pwd.append(parts[2])
                pointer = root
                for dir in pwd:
                    pointer = pointer["dirs"][dir]
    else:
        parts = line.strip().split(" ")
        if parts[0] == "dir":
            pointer["dirs"][parts[1]] = {"dirs": {}, "files": {}}
        else:
            pointer["files"][parts[1]] = parts[0]

def part1(root):
    sizes = []
    calc_sizes(root, sizes)
    total = 0
    for size in sizes:
        if size < 100000:
            total += size

    return total

def part2(root):
    max_file_space = 40000000
    smallest = max_file_space

    sizes = []
    total_used = calc_sizes(root, sizes)

    for size in sizes:
        if total_used - size > max_file_space:
            continue

        if size < smallest:
            smallest = size

    return smallest

print(f'part 1: %s' % part1(root))
print(f'part 2: %s' % part2(root))
