import re

input = open('input.txt', 'r')
inventory = []
instructions = []

for line in input:
    if "[" in line:
        stacks = re.findall("([\s\w\[\]]{3}\s?)", line)

        if len(inventory) == 0:
            inventory = [[] for x in range(len(stacks))]

        for i, crate in enumerate(stacks):
            if crate.strip() == "":
                continue
            inventory[i].append(crate.replace("[", "").replace("]", "").strip())
    elif line[0] == "m":
        instruction_parts = re.findall("(\d+)", line.strip())
        instructions.append([int(instruction_parts[0]), int(instruction_parts[1])-1, int(instruction_parts[2])-1])

class Crane:
    def __init__(self, inventory, instructions, model):
        self.inventory = inventory
        self.instructions = instructions

        self.reverse = False

        # stupid old model crane causing us to write legacy code
        if model == "9000":
            self.reverse = True

    def rearrange(self):
        for instruction in self.instructions:
            self.move(instruction[0], instruction[1], instruction[2])

        top_crates = ""
        for stack in self.inventory:
            top_crates += stack[0]

        return top_crates

    def move(self, quantity, source, destination):
        moving = self.inventory[source][0:quantity]
        if self.reverse:
            moving.reverse()
        self.inventory[destination] = moving + self.inventory[destination]
        self.inventory[source] = self.inventory[source][quantity:]

def part1(inventory, instructions):
    crane = Crane(inventory, instructions, "9000")
    return crane.rearrange()

def part2(inventory, instructions):
    crane = Crane(inventory, instructions, "9001")
    return crane.rearrange()

print(f'part 1: %s' % part1(inventory.copy(), instructions))
print(f'part 2: %s' % part2(inventory.copy(), instructions))