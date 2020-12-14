Conocimiento = [
	("Juan","San juan del rio"),
	("Alma","San juan del rio"),
	("Pamela","Tequisquiapan"),
	("Mary","Pachuca"),
	("Pachuca","Hidalgo"),
	("San Juan del Rio","Queretaro"),
	("Tequisquiapan","Queretaro"),
	("Queretaro","Mexico"),
	("Hidalgo","Mexico"),
	("Mexico","America")
]


def Esta(A,B,CON):
    i = 0
    while i != len(CON):
        if CON[i][0] == A:
            if CON[i][1] == B:
                return print(A,"Si Esta en",B)
            else:
                A = CON[i][1]
                i = i - 1
        i = i + 1
    else:
        return False


print (Esta("Juan","San juan el rio",Conocimiento))
