# GG
from motor  import checkEnd, enemyTurn, makeChange, printGrid
from player import myTurn

def init():
    cond = 0
    while cond == 0:
        playerPos = int(myTurn())
        makeChange(1,playerPos)
    
        enemyPos = int(enemyTurn())
        if enemyPos == -2:
            cond = -2
            break
        else:
            makeChange(-1,enemyPos)
    
        printGrid()
        cond = checkEnd()
    
    print(cond)
    
    
        
init()