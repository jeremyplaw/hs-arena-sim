import random

def randperf():
    return (random.random() + random.random() -
            random.random() - random.random())

def resolve(player_a):

    global pool
    global completed
    
    # if the player is done, take them out of the pool
    # and add them to the completed record
    if (player_a['losses'] == 3) or (player_a['wins'] == 12):
        completed.append(player_a)
        return
    
    # if the spot in the pool for that record is blank
    # put the player back in the pool to await an opponent
    if pool[player_a['wins']][player_a['losses']] is None:
        pool[player_a['wins']][player_a['losses']] = player_a
        return
    
    # if a player is in the pool with the same record play a match:
    player_b = pool[player_a['wins']][player_a['losses']]
    
    if ( player_a['str'] - player_b['str'] + randperf() > 0 ):
        winner = player_a
        loser = player_b
    else:
        winner = player_b
        loser = player_a

    # vacate the pool and add players to the pool at their new records
    # recursively resolve clashes if necessary

    pool[player_a['wins']][player_a['losses']] = None
    
    winner['wins'] = winner['wins'] + 1
    resolve(winner)
    
    loser['losses'] = loser['losses'] + 1
    resolve(loser)
    
    
def arena(nosim):
    global pool
    global completed
    
    # reset pool data structure: pool[#wins][#losses]
    pool = [[None]*3 for i in range(12)]
    completed = []

    for id in range(1,nosim):
        resolve({'id':id, 'wins':0, 'losses':0, 'str':randperf()+2 })
    
    f = open('arena.csv', 'w+')
    f.write('player id, strength, wins, losses\n')
    for player in completed:
        f.write( str(player['id']) +
                ', ' + str(player['str']) +
                ', ' + str(player['wins']) +
                ',' + str(player['losses']) +
                 '\n' )
    f.close()


arena(5000)

        
