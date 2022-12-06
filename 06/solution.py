input = open('input.txt', 'r')
buf = input.read()

def decode(buf, marker_len):
    for i, char in enumerate(buf):
        if i < marker_len-1:
            continue

        if len(set(buf[i - marker_len:i])) == marker_len:
            return i
    return -1

def part1(buf):
    return decode(buf, 4)

def part2(buf):
    return decode(buf, 14)

print(f'part 1: %s' % part1(buf))
print(f'part 2: %s' % part2(buf))