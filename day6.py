with open('day6.in','r') as f:
    lines = [l.strip() for l in f.readlines()]

a = set()
b = 0
for line in lines:
    if not len(line):
        b += len(a)
        a.clear()
        continue
    for c in line:
        a.add(c)


b += len(a)
print(b)

a = set([c for c in 'abcdefghijklmnopqrstuvwxyz'])
b = 0
for line in lines:
    if not len(line):
        b += len(a)
        a.clear()
        print("new group")
        for c in 'abcdefghijklmnopqrstuvwxyz':
            a.add(c)
        continue
    for c in 'abcdefghijklmnopqrstuvwxyz':
        if c not in line and c in a:
            print("removing ",c)
            a.remove(c)
    print("down to ", sorted("".join(a)))

b += len(a)
print(b)
