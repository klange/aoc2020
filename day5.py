with open('day5.in', 'r') as f:
    lines = [l.strip() for l in f.readlines()]

def process_row(seat):
    bottom = 0
    top = 128
    size = 128
    for c in seat[:7]:
        if c == 'F':
            top -= size // 2
        elif c == 'B':
            bottom += size // 2
        size = size // 2
    return bottom

def process_seat(seat):
    bottom = 0
    top = 8
    size = 8
    for c in seat[7:]:
        if c == 'L':
            top -= size // 2
        elif c == 'R':
            bottom += size // 2
        size = size // 2
    return bottom

print(process_row("FBFBBFFRLR"))
print(process_seat("FBFBBFFRLR"))

def seat_id(seat):
    row = process_row(seat)
    seat = process_seat(seat)
    return row * 8 + seat


top = -1

for l in lines:
    i = seat_id(l)
    if i > top:
        top = i

print(top)

taken = set()

for l in lines:
    i = seat_id(l)
    taken.add(i)

print ("---")

for i in range(min(taken),max(taken)):
    if (i - 1) in taken and (i + 1) in taken and i not in taken:
        print(i)
