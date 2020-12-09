with open('day9.in','r') as f:
    lines = [int(l.strip())  for l in f.readlines()]

sums = []

for i in range(25):
    me = lines[i]
    s = [me + x for x in lines[i+1:25]]
    out = (me, s)
    sums.append(out)

def find_value():
    for i in range(25, len(lines)):
        candidates = set()
        for _, x in sums:
            candidates = candidates.union(set(x))
        is_sum = lines[i] in candidates
        if not is_sum:
            return lines[i]
        else:
            sums.pop(0)
            for thing in sums:
                thing[1].append(thing[0] + lines[i])
            sums.append((lines[i], []))
    return None

value = find_value()

for i in range(len(lines)):
    for j in range(i+2,len(lines)):
        if sum(lines[i:j]) == value:
            print(i,j,min(lines[i:j]),max(lines[i:j]),min(lines[i:j])+max(lines[i:j]))
