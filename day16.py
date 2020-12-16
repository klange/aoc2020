fields, errors, my_ticket, muldep = {}, 0, [], 1
bad = lambda v, f: (v < f[0][0] or v > f[1][1]) or (v > f[0][1] and v < f[1][0])
process = lambda t, cs: [set(f for f in cs[i] if not bad(v, fields[f])) for i, v in enumerate(t)]
with open('day16.in','r') as f: defs, me, others = map(lambda lines: [line.strip() for line in lines.split('\n')], f.read().strip().split('\n\n'))
fields = {name: [[int(x) for x in f.split('-', 1)] for f in data.split(' or ', 1)] for (name, data) in map(lambda f: f.split(": ", 1), defs)}
base = [set(fields.keys()) for i in range(len(fields))]
my_ticket.extend([int(x) for x in me[1].split(',')])
candidates = process(my_ticket, base)
for ticket, cs in [(ticket, process(ticket, base)) for ticket in [[int(x) for x in l.split(',')] for l in others[1:]]]:
    candidates, errors = process(ticket, candidates) if all(len(c) for c in cs) else candidates, errors + sum(v for i, v in enumerate(ticket) if not len(cs[i]))
while not all(len(c) == 1 for c in candidates):
    for hits, f in [([i for i, c in enumerate(candidates) if (len(c) == 1 and f in c)], f) for f in fields.keys()]:
        list(map(lambda j: candidates[j].remove(f), [i for i, c in enumerate(candidates) if hits and i != hits[0] and f in c]))
for d in [v for i, v in enumerate(my_ticket) if next(iter(candidates[i])).startswith('departure')]:
    muldep *= d
print(errors, muldep)
