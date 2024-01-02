import random

thislist = [0, 0, 0, 0, 0, 0, 0, 0, 0]

def makeChange(player,pos):
    thislist[pos-1] = player
    
def printGrid():
    print(str(thislist[0])+ " " + str(thislist[1]) + " " + str(thislist[2]))
    print(str(thislist[3])+ " " + str(thislist[4]) + " " + str(thislist[5]))
    print(str(thislist[6])+ " " + str(thislist[7]) + " " + str(thislist[8]))
    
def checkEnd():
    l1 = int(thislist[0]) + int(thislist[1]) + int(thislist[2])
    l2 = int(thislist[3]) + int(thislist[4]) + int(thislist[5])
    l3 = int(thislist[6]) + int(thislist[7]) + int(thislist[8])
    
    c1 = int(thislist[0]) + int(thislist[3]) + int(thislist[6])
    c2 = int(thislist[1]) + int(thislist[4]) + int(thislist[7])
    c3 = int(thislist[2]) + int(thislist[5]) + int(thislist[8])
    
    d1 = int(thislist[0]) + int(thislist[4]) + int(thislist[8])
    d2 = int(thislist[2]) + int(thislist[4]) + int(thislist[6])
    
    if l1 == 3 or l2 == 3 or l3 == 3 or c1 == 3 or c2 == 3 or c3 == 3 or d1 == 3 or d2 == 3:
        return 1
    elif l1 == -3 or l2 == -3 or l3 == -3 or c1 == -3 or c2 == -3 or c3 == -3 or d1 == -3 or d2 == -3:
        return -1
    else:
        return 0
    
def enemyTurn():
    enemylist = []
    for x in range(len(thislist)):
        if thislist[x] == 0:
            enemylist.append(x+1)
    if len(thislist) != 0:        
        posEnemy = random.choice(enemylist)
    else:
        posEnemy = -2   
        
    return posEnemy