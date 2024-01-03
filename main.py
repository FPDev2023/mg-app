# GG
from file import findResult, readFile, writeFile
from motor  import checkEnd, enemyTurn, makeChange, nog, printGrid, resetG
from player import myTurn

def initG():
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
    
def initL():
    for x in range(5):
        cond = 0
        while cond == 0:
            #playerPos = int(myTurn())
            #makeChange(1,playerPos)
            
            enemyPos1 = int(enemyTurn())
            if enemyPos1 == -2:
                cond = -2
                break
            else:
                makeChange(1,enemyPos1)
    
            enemyPos = int(enemyTurn())
            if enemyPos == -2:
                cond = -2
                break
            else:
                makeChange(-1,enemyPos)
    
            printGrid()
            if cond == -2:
                nog()
                cond = 0
            else:
               cond = checkEnd()
    
        print("Round: "+str(x)+" => "+str(cond))
        resetG()
        
initL()