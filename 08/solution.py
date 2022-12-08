input = open('input.txt', 'r')
grid = []

for line in input:
    grid.append(list(map(lambda x: int(x), list(line.strip()))))

def eval_tree(grid, row, col, val):
    # up
    up = True
    up_vis = 0
    rows = grid[:row]
    rows.reverse()
    for trees in rows:
        up_vis += 1
        if trees[col] >= val:
            up = False
            break

    # right
    right = True
    right_vis = 0
    for tree in grid[row][col + 1:]:
        right_vis += 1
        if tree >= val:
            right = False
            break

    # down
    down = True
    down_vis = 0
    for trees in grid[row + 1:]:
        down_vis += 1
        if trees[col] >= val:
            down = False
            break

    #left
    left = True
    left_vis = 0
    trees = grid[row][:col]
    trees.reverse()
    for tree in trees:
        left_vis += 1
        if tree >= val:
            left = False
            break

    return left or right or up or down, right_vis * left_vis * up_vis * down_vis

total_visible = 2 * (len(grid) + len(grid[0])) - 4
top_score = 0

for i, row in enumerate(grid[1:len(grid)-1], start=1):
    for j, tree in enumerate(row[1:len(row)-1], start=1):
        visible, score = eval_tree(grid, i, j, tree)

        if visible:
            total_visible += 1

        if score > top_score:
            top_score = score

print(f'part 1: %s' % total_visible)
print(f'part 2: %s' % top_score)