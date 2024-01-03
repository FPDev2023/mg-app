import os


def readFile(namefile):
    list = []
    if os.path.exists(namefile):
        f = open(namefile,"r")
        nl = int(f.readline())
    
        if nl > 0:
            for x in range(nl):
                list.append((f.readline()).replace("\n",""))
    else:
        f = open(namefile, "x")
        
    f.close()
    return list

def findResult(namefile,result):
    list = []
    if os.path.exists(namefile):
        f = open(namefile,"r")
        nl = int(f.readline())
    
        if nl > 0:
            for x in range(nl):
                list.append((f.readline()).replace("\n",""))
    else:
        f = open(namefile, "x")
        
    f.close()
    
    for x in range(len(list)):
        if list[x] == result:
            return 1
    
    return 0

def writeFile(namefile,result):
    list = []
    if os.path.exists(namefile):
        f = open(namefile,"r")
        nl = int(f.readline())
    
        if nl > 0:
            for x in range(nl):
                list.append((f.readline()).replace("\n",""))
    else:
        f = open(namefile, "x")
        
    f.close()
    
    f = open(namefile, "w")
    l = nl + 1
    text = str(l) + "\n"
    for x in range(nl):
        text = text + list[x] + "\n"
    text = text + result + "\n"
    f.write(text)
    f.close()
    
