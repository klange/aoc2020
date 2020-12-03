with open('day3.in', 'r') as f:
    lines = [l.strip() for l in f.readlines()]


def count_trees(lines, x_off, y_off):
    modulo = len(lines[0])
    x = 0
    y = 0
    trees = 0
    while y < len(lines):
        if lines[y][x % modulo] == '#':
            trees += 1
        x += x_off
        y += y_off
    return trees

print("part 1:", count_trees(lines, 3, 1))

print("part 2:",
        count_trees(lines, 1, 1) *
        count_trees(lines, 3, 1) *
        count_trees(lines, 5, 1) *
        count_trees(lines, 7, 1) *
        count_trees(lines, 1, 2))
