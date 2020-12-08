with open('day8.in','r') as f:
    lines = [l.strip() for l in f.readlines()]

print(len(lines))

def tryIt(lines):
    ip = 0
    acc = 0
    visited = set()
    while True:
        if ip == len(lines):
            return True, acc
        if ip > len(lines):
            print("??? bad jump past end of code")
            return False, acc
        instr, arg = lines[ip].split(' ',1)
        visited.add(ip)
        if instr == 'jmp':
            ip += int(arg)
        else:
            if instr == 'acc':
                acc += int(arg)
            ip += 1
        if ip in visited:
            print(acc)
            return False, acc

for i in range(len(lines)):
    if lines[i].startswith('jmp'):
        worked, acc = tryIt(lines[:i] + [lines[i].replace('jmp','nop')] + lines[i+1:])
        if worked:
            print("Change",i,"to nop")
            print(acc)
            break
    elif lines[i].startswith('nop'):
        worked, acc = tryIt(lines[:i] + [lines[i].replace('nop','jmp')] + lines[i+1:])
        if worked:
            print("Change",i,"to jmp")
            print(acc)
            break
    else:
        continue
