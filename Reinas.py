
mtz=[[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0]]
posAct=[]
llave = 0

posiciones = [[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0]]
def entrada(nreinas, mtz, llave,posiciones):
    backup = [[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0]]
    cont = 0
    print("nreinas "+str(nreinas))
 
    if nreinas == 1:
        return solucion(mtz)
    else: 
        for t in range(len(mtz)):
            for r in range(len(mtz[t])):
                
                if cont == 0:
					
                    if posiciones[t][r] != 3:
                        if(mtz[t][r] == 0):

                            if nreinas == 4:
                                posiciones[t][r] = 3
                            mtz[t][r] = 1
                            cont = cont + 1
                            posAct.append([t,r])

        mtz = iterar(mtz,posAct)

        posAct.pop(0)
        for t in mtz:

            if 0 in t:
                llave = 0
            else:
                llave = 1
        if llave == 1:
            print(llave)
            for t in backup:
                print(t)
            nreinas=4
            llave=0
            return entrada(nreinas,backup,llave,posiciones)
        if llave == 0:
            print(llave)
            nreinas=nreinas-1
            return entrada(nreinas,mtz,llave,posiciones)
        
def iterar(mtz,posAct):
    print("************")
    a = posAct[0][0]
    b = posAct[0][1]
    r = range(len(mtz))
    bb = b
    aa = a
    print(posAct)
    
    for t in range(len(mtz)):
        for r in range(len(mtz[t])):
            mtz[a][r] = 2
            mtz[t][b] = 2
    imp(mtz)
    for t in range(len(mtz)):
        bb = bb-1
        aa = aa -1
        if (bb >= 0)and(aa >=0):
            print("- -")
            mtz[aa][bb] = 2
    bb = b
    aa = a
    imp(mtz)
    for t in range(len(mtz)):
        aa = aa +1
        bb = bb +1
        if (aa <= r)and(bb <= r):
            print("+ +")
            mtz[aa][bb] = 2

    bb = b
    aa = a
    imp(mtz)
    for t in range(len(mtz)):
        bb = bb+1
        aa = aa -1
        if (bb < r)and(aa >=0):
            print("+ -")
            mtz[aa][bb] = 2
    bb = b
    aa = a
    imp(mtz)
    for t in range(len(mtz)):
        bb = bb-1
        aa = aa + 1
        if (bb >= 0)and(aa <r):
            print("- +")
            mtz[aa][bb] = 2
    mtz[a][b]=1
    imp(mtz)
    print("************")
    return mtz
    
def solucion(matriz):
    for t in range(len(matriz)):
        for r in range(len(matriz[t])):
            if (matriz[t][r]) == 0:
                 matriz[t][r] = 1
    print("****resultado****")
    for t in matriz:
        print(t)

def imp(matriz):
    print("************")
    for t in matriz:
        print(t)

entrada(4,mtz,0,posiciones)