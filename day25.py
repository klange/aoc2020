with open('day25.in','r') as f: lines = [x.strip() for x in f.readlines()]

card = int(lines[0])
door = int(lines[1])

def findLoopSize(key, sn):
    l = 0
    i = 1
    while key != i:
        l += 1
        i = (i * sn) % 20201227
    return l

def doLoop(sn, loops):
    i = 1
    for j in range(loops):
        i = (i * sn) % 20201227
    return i

cardLoops = findLoopSize(card,7)
doorLoops = findLoopSize(door,7)

eKey1 = doLoop(card,doorLoops)
eKey2 = doLoop(door,cardLoops)
print(eKey1,eKey2)
