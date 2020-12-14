Conocimiento = [
	("Tortuga","Proteccion Queratina"),
    ("Tortuga","Agua"),
    ("Tortuga","Tierra"),
    ("Tortuga","Oviparo"),
    ("Tortuga","Vertebrados"),
    ("Tortuga","Sauropsidos"),
    ("Gallo","Proteccion Queratina"),
    ("Gallo","Garras"),
    ("Gallo","Oviparo"),
    ("Gallo","Tierra"),
    ("Gallo","Vertebrado"),
    ("Gallo","Sauropsidos"),
    ("Cocodrilo","Proteccion Queratina"),
    ("Cocodrilo","Garras"),
    ("Cocodrilo","Agua"),
    ("Cocodrilo","Tierra"),
    ("Cocodrilo","Oviparo"),
    ("Cocodrilo","Vertebrado"),
    ("Cocodrilo","Tetrapodo"),
    ("Cocodrilo","Sauropsidos"),
    ("Iguana","Proteccion Queratina"),
    ("Iguana","Garras"),
    ("Iguana","Oviparo"),
    ("Iguana","Vertebrado"),
    ("Iguana","Sauropsidos"),
    ("Iguana","Tetrapodo"),    
    ("Gato","Pelo"),
    ("Gato","G Mamarias"),
    ("Gato","Garras"),    
    ("Gato","Tierra"),
    ("Gato","Viviparo"),    
    ("Gato","Vertebrado"),
    ("Gato","Tetrapodo"),
    ("Oso","Mammalia"),
    ("Ballena","Proteccion Queratina"),
    ("Ballena","Agua"),
    ("Ballena","Viviparo"),
    ("Ballena","Vertebrado"),
    ("Oso","Mammalia"),
    ("Oso","G Mamarias"),
    ("Oso","Pelo"),
    ("Oso","Garras"),
    ("Oso","G Mamarias"),
    ("Oso","Tierra"),
    ("Oso","Viviparo"),
    ("Oso","Vertebrado"),
    ("Oso","Tetrapodo"),
    ("Oso","Mammalia"),
    ("Delfin","Agua"),
    ("Delfin","Viviparo"),
    ("Delfin","Vertebrado"),
    ("Delfin","Mammalia")
]

def tve(A,B,C,CON):
    if not CON:
        return False
    if A=="Tiene":
        def tiene(D,E,CON2):
            D==B
            E==C
            CON2==CON
            i = 0
            while i != len(CON):
                if CON[i][0] == D:
                    if CON[i][1] == E:
                        return True
                    else:
                        D = CON[i][1]
                        i = i - 1
                i = i + 1
    if A=="Vive":
        def vive(F,G,CON3):
            F==B
            G==C
            CON3==CON
            i = 0
            while i != len(CON):
                if CON[i][0] == F:
                    if CON[i][1] == G:
                        return True
                    else:
                        F = CON[i][1]
                        i = i - 1
                i = i + 1
    if A=="Es":
        def es(H,J,CON4):
            H==B
            J==C
            CON4==CON
            i = 0
            while i != len(CON):
                if CON[i][0] == H:
                    if CON[i][1] == J:
                        return True
                    else:
                        H = CON[i][1]
                        i = i - 1
                i = i + 1
                                        

print (tve("Es","Delfin","Agua",Conocimiento))
            
            
            