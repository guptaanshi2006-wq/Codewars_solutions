def duck_duck_goose(players, goose):
    if goose%len(players)==1:
        return players[0].name
    elif goose%len(players)==2:
        return players[1].name
    elif goose%len(players)==3:
        return players[2].name
    elif goose%len(players)==0:
        return players[-1].name
    else:
        return players[goose%len(players)-1].name
    