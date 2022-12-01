input = open('input.txt', 'r')
lines = input.readlines()

elves = [0,0,0]

elf_total = 0
max_callories = 0

for line in lines:
    if line.strip() == "":
        elves.append(elf_total)
        elves.sort(reverse=True)
        elves.pop()
        elf_total = 0
    else:
        elf_total += int(line)

print(sum(elves))
