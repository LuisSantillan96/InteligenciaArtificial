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
def esta(A,B,CON):
	 if not CON:
		 return False
     Elemento = [ e for e in CON if e[0] == A]
	 if not Elemento:
		 return False
	 Elemento = Elemento[0]
	 if Elemento[1] == B:
		 return True
	 return esta(Elemento[1],B,CON)

print (esta("Juan","San Juan del Rio",Conocimiento))


