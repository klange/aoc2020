n = [0,3,6] # [15,5,1,4,7,0]

last = {}
for i in range(len(n)-1):
    last[n[i]] = i

latest = n[-1]
turn = len(n)
while True:
    if latest not in last:
        last[latest] = turn - 1
        latest = 0
    else:
        i = turn - last[latest] - 1
        last[latest] = turn - 1
        latest = i
    turn += 1
    if turn == 30000000: # 2020
        print(turn, latest)
        break

