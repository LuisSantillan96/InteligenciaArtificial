# HECHO POR:
    #MENDOZA TREJO JAIRO
    #SANTILLAN OLVERA LUIS ANGEL
    

Es=[
    ("Tortuga","Oviparo"),
    ("Tortuga","Vertebrados"),
    ("Tortuga","Sauropsidos"),
    ("Gallo","Oviparo"),
    ("Gallo","Vertebrado"),
    ("Gallo","Sauropsidos"),
    ("Cocodrilo","Oviparo"),
    ("Cocodrilo","Tetrapodo"),
    ("Cocodrilo","Sauropsidos"),
    ("Iguana","Oviparo"),
    ("Iguana","Sauropsidos"),
    ("Iguana","Tetrapodo"),
    ("Gato","Viviparo"),
    ("Gato","Vertebrado"),
    ("Gato","Tetrapodo"),
    ("Oso","Mammalia"),
    ("Ballena","Viviparo"),
    ("Ballena","Vertebrado"),
    ("Oso","Viviparo"),
    ("Oso","Vertebrado"),
    ("Oso","Tetrapodo"),
    ("Oso","Mammalia"),
    ("Delfin","Viviparo"),
    ("Delfin","Vertebrado"),
    ("Delfin","Mammalia")
]

Vive=[
    ("Tortuga","Tierra"),
    ("Tortuga","Agua"),
    ("Gallo","Tierra"),
    ("Cocodrilo","Agua"),
    ("Cocodrilo","Tiera"),
    ("Iguana","Tierra"),
    ("Gato","Tierra"),
    ("Ballena","Agua"),
    ("Oso","Tierra"),
    ("Delfin","Agua"),
]
     
Tiene=[
    ("Tortuga","Garras"),
    ("Tortuga","Proteccion Queratina"),
    ("Gallo","Proteccion Queratina"),
    ("Gallo","Garras"),
    ("Cocodrilo","Garras"),
    ("Cocodrilo","Proteccion Queratina"),
    ("Iguana","Proteccion Queratina"),
    ("Gato","G Mamarias"),
    ("Gato","Garras"),
    ("Gato","Pelo"),
    ("Gato","G Mamarias"),
    ("Gato","Garras"),
    ("Gato","Pelo"),
    ("Tortuga","Proteccion Queratina"),    
]
 

def Ess(A,B,CON):
    if not CON:
        return False
    i = 0
    while i<len(CON):
        if CON[i][0]==A:
            if CON[i][1]==B:
                return True
            A=CON[i][1]
            
        i=i+1
    return False

def Vivee(A,B,CON):
    if not CON:
        return False
    x = 0
    while x<len(CON):
        if CON[x][0]==A:
            if CON[x][1]==B:
                return True
            
        x=x+1
    return False

def Tienee(A,B,CON):
    if not CON:
        return False
    t = 0
    while t<len(CON):
        if CON[t][0]==A:
            if CON[t][1]==B:
                return True
            
        t=t+1
    return False

print (Ess("Gallo","Oviparo",Es))
print (Tienee("Tortuga","Proteccion Queratina",Tiene))
print (Vivee("Delfin","Agua",Vive))