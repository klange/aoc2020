with open('day16.in','r') as f:
    lines = [x.strip() for x in f.readlines()]

fields = {}
process = 0
errors = 0
my_ticket = []
valid_tickets = []

def process_ticket(ticket, candidates):
    for i in range(len(ticket)):
        remove = []
        v = ticket[i]
        for field in candidates[i]:
            ((a,b), (c,d)) = fields[field]
            if (v < a or v > d) or (v > b and v < c):
                remove.append(field)
        for c in remove:
            candidates[i].remove(c)

def validate_ticket(ticket):
    cs = [set(fields.keys()) for i in range(len(fields))]
    process_ticket(ticket, cs)
    return all([len(c) > 0 for c in cs]), sum(ticket[i] for i in range(len(ticket)) if not len(cs[i]))

for line in lines:
    if not len(line):
        process += 1
        continue
    if process == 0:
        name, data = line.split(": ", 1)
        first, second = data.split(" or ", 1)
        (a, b) = [int(x) for x in first.split('-',1)]
        (c, d) = [int(x) for x in second.split('-',1)]
        fields[name] = ((a,b),(c,d))
    elif process == 1:
        if not line.startswith('your ticket'):
            my_ticket.extend([int(x) for x in line.split(',')])
    elif process == 2:
        if not line.startswith('nearby tickets'):
            ticket = [int(x) for x in line.split(',')]
            s, e = validate_ticket(ticket)
            errors += e
            if s:
                valid_tickets.append(ticket)

candidates = [set(fields.keys()) for i in range(len(fields))]
valid_tickets.append(my_ticket)
for ticket in valid_tickets:
    process_ticket(ticket, candidates)

while True:
    made_progress = 0
    for f in fields.keys():
        hits = [i for i in range(len(candidates)) if (len(candidates[i]) == 1 and f in candidates[i])]
        for j in [x for x in range(len(candidates)) if hits and x != hits[0] and f in candidates[x]]:
            candidates[j].remove(f)
            made_progress = 1
    if all(len(c) == 1 for c in candidates) or not made_progress:
        break

muldep = 1
for d in [my_ticket[i] for i in range(len(my_ticket)) if any(x.startswith('departure') for x in candidates[i])]:
    muldep *= d

print(errors)
print(muldep)
