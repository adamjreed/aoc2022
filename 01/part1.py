input = open('input.txt', 'r')
lines = input.readlines()

elf_total = 0
max_callories = 0

for line in lines:
    if line.strip() == "":
        if elf_total > max_callories:
            max_callories = elf_total
        elf_total = 0
    else:
        elf_total += int(line)

print(max_callories)
