with open('day14.in','r') as f:
    lines = [x.strip() for x in f.readlines()]

def apply_mask(mask, val):
    valb = "{0:036b}".format(int(val))
    return int(''.join([valb[i] if mask[i] == 'X' else mask[i] for i in range(len(mask))]), 2)

mem = {}
current_mask = "X" * 36
for line in lines:
    if line.startswith("mask = "):
        current_mask = line[7:]
    else:
        addr, val = line[4:].split("] = ", 1)
        mem[int(addr)] = apply_mask(current_mask, val)

print(sum([value for value in mem.values()]))

def mask_to_addresses(mask, addr):
    if not 'X' in mask:
        raise ValueError()
    addrb = "{0:036b}".format(int(addr))
    counts = sum([1 for x in mask if x == 'X'])
    back = {}
    j = 0
    for i in range(len(mask)):
        if mask[i] == 'X':
            back[i] = j
            j += 1
    for i in range(2 ** counts):
        bits = "{0:b}".format(i).zfill(counts)
        yield int(''.join([
            ('1' if mask[j] == '1' else
            (addrb[j] if mask[j] == '0' else
            (bits[back[j]]))) for j in range(len(mask))]), 2)

current_mask = "X" * 36
mem = {}
for line in lines:
    if line.startswith("mask = "):
        current_mask = line[7:]
        #print("mask is",current_mask,"should yield",2**sum([1 for m in current_mask if m == 'X']))
    else:
        addr, val = line[4:].split("] = ", 1)
        i = 0
        for addr in mask_to_addresses(current_mask, addr):
            #print('{0:036b}'.format(addr),val)
            mem[addr] = int(val)
            i += 1
        #print("wrote",i,"addresses")
print(len(mem.values()))
print(sum([value for value in mem.values()]))
