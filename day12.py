with open('day12.in','r') as f:
    lines = [l.strip()  for l in f.readlines()]

way_x = 10
way_y = 1
ship_x = 0
ship_y = 0

def rel(a, b):
    return b - a

for line in lines:
    cmd, val = line[0], line[1:]
    val = int(val)
    if cmd == 'N':
        way_y += val
    elif cmd == 'E':
        way_x += val
    elif cmd == 'S':
        way_y -= val
    elif cmd == 'W':
        way_x -= val
    elif cmd == 'L':
        if val == 90:
            way_x, way_y = -way_y, way_x
        elif val == 180:
            way_x, way_y = -way_x, -way_y
        elif val == 270:
            way_x, way_y = way_y, -way_x
        else:
            raise ValueError(val)
    elif cmd == 'R':
        if val == 270:
            way_x, way_y = -way_y, way_x
        elif val == 180:
            way_x, way_y = -way_x, -way_y
        elif val == 90:
            way_x, way_y = way_y, -way_x
        else:
            raise ValueError(val)
    elif cmd == 'F':
        ship_x += way_x * val
        ship_y += way_y * val
    print(cmd, val, ship_x, ship_y, abs(ship_x) + abs(ship_y))
