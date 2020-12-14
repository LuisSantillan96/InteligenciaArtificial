from io import open
import json
Conocimiento = False

with open("basefedelobo.json", "r") as read_file:
    data=json.load(read_file)
    Conocimiento=data['probabilidad']
    
archivo = open('tweet.txt','r')
t1 = archivo.read()
t2 = t1.split()
archivo.close()

def stream(t, CON):
    suma=0.0
    promedio=0.0
    l = len(t)
    k = len(CON)
    comparacion = []
    if l <= 2:
        return "El tweet no puede ser evaluado"
    else:
        for i in range(l):
            for j in range(k):
                if CON [j][0]==t[i]:
                    comparacion.append(CON[j])
            for l in range(len(comparacion)):
                suma += float(comparacion[l][1])
                promedio = suma / len(comparacion)
            if (promedio > .55):
                return "stream"
            else:
                return "No es stream"
            
print(stream(t2,Conocimiento))

