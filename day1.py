"""
with open('day1.in','r') as f:
    lines = [int(x) for x in f.readlines()]
    data = set(lines)
    for line in lines:
        if (2020 - line) in data:
            print(line, 2020 - line, (line) * (2020 - line))
"""

# Part 2

with open('day1.in','r') as f:
    lines = [int(x) for x in f.readlines()]

def sums_index(lines, ind):
    for line in lines[:ind]:
        yield line + lines[ind]
    for line in lines[ind:]:
        yield line + lines[ind]

for ind in range(len(lines)):
    for s in sums_index(lines, ind):
        if (2020 - s) in lines:
            print((s - lines[ind]) * lines[ind] * (2020 - s))
