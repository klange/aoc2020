n = [0,3,6] # [15,5,1,4,7,0]
seen, last = {i: x+1 for x, i in enumerate(n)}, n[-1]
for turn in range(len(n),30000000): # 2020
    seen[last], last = turn, turn - seen.get(last,turn)
print(last)
