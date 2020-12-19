with open('day19.in','r') as f:
    lines = [x.strip() for x in f.readlines()]

rules = {}

rule_count = 0
for line in lines:
    if not len(line):
        break
    name, rule = line.split(": ", 1)
    rules[int(name)] = [[(x[1] if x[0] == '"' else int(x)) for x in s.split()] for s in rule.split(" | ")]
    rule_count += 1

def matches(rule, s):
    if isinstance(rule, str):
        if len(s) > 0 and s[0] == rule:
            return 1
        else:
            return -1
    for subrule in rules[rule]:
        consumed = 0
        for token in subrule:
            c = matches(token, s[consumed:])
            if c == -1:
                consumed = -1
                break
            consumed += c
        if consumed > 0:
            return consumed
    return -1

good = 0
for line in lines[rule_count+1:]:
    if matches(0, line) == len(line):
        good += 1
print(good)
good = 0

def matches_at_most(s, n):
    c = 0
    t = 0
    while True:
        x = matches(31, s[c:])
        if x == -1:
            return 0
        t += 1
        c += x
        if t > n:
            return 0
        if not s[c:]:
            return 1
    return 0

for line in lines[rule_count+1:]:
    c = matches(42, line)
    if (c == -1):
        continue
    d = matches(42, line[c:])
    if (d == -1):
        continue
    n = 1
    x = c + d
    while True:
        if matches_at_most(line[x:], n):
            good += 1
            break
        else:
            c = matches(42, line[x:])
            if c < 1:
                break
            else:
                x += c
                n += 1

print(good)
