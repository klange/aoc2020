fields, process, errors, my_ticket, tickets, valid_tickets = {}, 0, 0, [], [], []

with open('day16.in','r') as f:
    for line in [x.strip() for x in f.readlines()]:
        if not len(line):
            process += 1
            continue
        if process == 0:
            name, data = line.split(": ", 1)
            fields[name] = [[int(x) for x in f.split('-', 1)] for f in data.split(' or ', 1)]
        elif process == 1 and not line.startswith('your ticket'):
            my_ticket.extend([int(x) for x in line.split(',')])
        elif process == 2 and not line.startswith('nearby tickets'):
            tickets.append([int(x) for x in line.split(',')])

bad = lambda v, f: (v < f[0][0] or v > f[1][1]) or (v > f[0][1] and v < f[1][0])
process = lambda t, cs: [set([ f for f in cs[i] if not bad(t[i], fields[f])] ) for i in range(len(t)) ]

def validate_ticket(ticket):
    cs = process(ticket, [set(fields.keys()) for i in range(len(fields))])
    return all([len(c) > 0 for c in cs]), sum(ticket[i] for i in range(len(ticket)) if not len(cs[i]))

for ticket in tickets:
    s, e = validate_ticket(ticket)
    if s: valid_tickets.append(ticket)
    else: errors += e

candidates = [set(fields.keys()) for i in range(len(fields))]
for ticket in valid_tickets + [my_ticket]:
    candidates = process(ticket, candidates)

while not all(len(c) == 1 for c in candidates):
    for f in fields.keys():
        hits = [i for i in range(len(candidates)) if (len(candidates[i]) == 1 and f in candidates[i])]
        for j in [x for x in range(len(candidates)) if hits and x != hits[0] and f in candidates[x]]:
            candidates[j].remove(f)

muldep = 1
for d in [my_ticket[i] for i in range(len(my_ticket)) if any(x.startswith('departure') for x in candidates[i])]:
    muldep *= d

print(errors, muldep)
