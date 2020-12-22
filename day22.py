with open('day22.in','r') as f: lines = [x.strip() for x in f.readlines()]
getPlayers = lambda: {1: [int(x) for x in lines[1:lines.index("")]], 2: [int(x) for x in lines[lines.index("")+2:]]}
scorePlayer = lambda player: sum([card * (index + 1) for index, card in enumerate(player[::-1])])

players = getPlayers()
while players[1] and players[2]:
    a, b = players[1].pop(0), players[2].pop(0)
    players[1 if a > b else 2].extend(sorted([a,b])[::-1])
print(scorePlayer(players[1] + players[2]))

def playGame(players):
    rounds = set()
    while players[1] and players[2]:
        if (tuple(players[1]),tuple(players[2])) in rounds: return 1
        rounds.add((tuple(players[1]),tuple(players[2])))
        a, b = players[1].pop(0), players[2].pop(0)
        winner = playGame({1: players[1][:a] ,2: players[2][:b]}) if (len(players[1]) >= a and len(players[2]) >= b) else (1 if a > b else 2)
        players[winner].extend([a,b] if winner == 1 else [b,a])
    return 1 if players[1] else 2
players = getPlayers()
print(scorePlayer(players[playGame(players)]))
