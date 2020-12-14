# HECHO POR:
    #MENDOZA TREJO JAIRO
    #SANTILLAN OLVERA LUIS ANGEL

import json
Conocimiento = False

with open("baseanimales.json", "r") as read_file:
    data = json.load(read_file)
    Conocimiento = data['CONOCIMIENTO']

def animales(A, B,C, CON):
    r = 0
    l = len(CON)
    while r != l:
        if CON[r][0] == A:
            if CON[r][1] == B:
                if CON[r][2] == C:
                    return print("Es Verdadero!!")
        r += 1
    else:
        return print("Es Falso!")
    
def animales_b(A,B,C):
    return animales(A,B,C,Conocimiento)

def main():
    print('Notacion De Busqueda --> animales_b("Animal","Es/Tiene/Vive","Question")')
    print("Para Salir Oprime q ó Escribiendo quit()")
    Terminar = False
    while not Terminar:
        Leer = input("> ")
        if Leer == 'q':
            return
        Imprimir = eval(Leer)
        print(Imprimir)

if __name__ == '__main__':
    main()
