import random
from file import findResult, readFile, writeFile

thislist = [0, 0, 0, 0, 0, 0, 0, 0, 0]

def resetG():
    global thislist 
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
        saveG(0)
        return 1
    elif l1 == -3 or l2 == -3 or l3 == -3 or c1 == -3 or c2 == -3 or c3 == -3 or d1 == -3 or d2 == -3:
        saveG(1)
        return -1
    else:
        return 0
    
def nog():
    saveG(2)
    
def enemyTurn():
    enemylist = []
    for x in range(len(thislist)):
        if thislist[x] == 0:
            enemylist.append(x+1)
    if len(enemylist) != 0:
        print(len(enemylist))        
        posEnemy = random.choice(enemylist)
    else:
        posEnemy = -2   
        
    return posEnemy

def saveG(result):
    
    text=""
    for x in thislist:
        if (str(thislist[x]) == "-1"):
            text = text + "2"
        else:
            text = text + str(thislist[x])
    
    if findResult("ml.txt",text[0:8]) == 0:
        writeFile("ml.txt",text+str(result))