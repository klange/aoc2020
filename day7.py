with open('day7.in','r') as f:
    lines = [l.strip() for l in f.readlines()]

descriptions = {}

for line in lines:
    mine, contains = line.split(" bags contain ", 1)
    mine = mine.strip()
    if contains.startswith('no other'):
        descriptions[mine] = []
    else:
        contents = []
        for bag in contains.split(", "):
            cnt, rest = bag.split(' ',1)
            name, _, _ = rest.strip().rpartition('bag')
            for i in range(int(cnt)):
                contents.append(name.strip())
        descriptions[mine] = contents

def reaches(bag, target, seen=None):
    if seen == None:
        seen = set([bag])
    for n in descriptions[bag]:
        if n == target:
            return True
        if n not in seen:
            seen.add(n)
            if reaches(n, target, seen): return True
    return False

count = 0
for bag in descriptions.keys():
    if reaches(bag, 'shiny gold'):
        count += 1

print("There are",count,"bags that can contain a shiny gold bag, eventually.")

def find_depth(bag):
    if not len(descriptions[bag]):
        return 0
    to_scan = descriptions[bag]
    count = 0
    while to_scan:
        i = to_scan.pop(0)
        count += 1
        to_scan.extend(descriptions[i])
    return count

print("A shiny gold bag contains", find_depth('shiny gold'), "bags.")
