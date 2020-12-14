#https://runestone.academy/runestone/static/pythoned/Recursion/ExploracionDeUnLaberinto.html
#https://gist.github.com/knkillname/60779628155ef113be3f6537c1c75b19
#http://razonartificial.com/2010/01/buscador-de-caminos-con-python/
#https://www.iteramos.com/pregunta/8113/representar-y-resolver-un-laberinto-dado-una-imagen
#https://jariasf.wordpress.com/2012/02/27/algoritmo-de-busqueda-breadth-first-search/
import json, queue, random

#https://www.geeksforgeeks.org/queue-in-python/
with open ("mapa.json","r") as read_file:
	data = json.load(read_file)
	sm = data['Mapa']

    #boome = "R"
print('*** I: Izquierda | D: Derecha | B: Abajo | A: Arriba ***')
def ruta(Mapa, path=""):
    #https://www.geeksforgeeks.org/enumerate-in-python/
	for i, pos in enumerate(sm[0]):
		if pos == "R":
			inicio = i
	i = inicio
	y = 0
	pos = set()
	for mov in path:
		if mov == "I":
			i -= 1
		if mov == "D":
			i += 1
		if mov == "A":
			y -= 1
		if mov == "B":
			y += 1
		pos.add((y, i))

	for y, fila in enumerate(sm):
		for i, col in enumerate(fila):
			if (y, i) in pos:
                # # maraca el camino
				print("# ", end="")
			else:
				print(col + " ", end="")
		print()
def valida(sm, camino):
	for i, pos in enumerate(sm[0]):
		if pos == "R":
			inicio = i
	i = inicio
	y = 0
	for mov in camino:
		if mov == "I":
			i -= 1
		if mov == "D":
			i += 1
		if mov == "A":
			y -= 1
		if mov == "B":
			y += 1
		if not(0 <= i < len(sm[0]) and 0 <= y < len(sm)):
			return False
        # son los obtaculos
		if (sm[y][i] == "*"):
			return False
	return True
def final(sm, camino):
	for i, pos in enumerate(sm[0]):
		if pos == "R":
			start = i
	i = start
	y = 0
	for mov in camino:
		if mov == "I":
			i -= 1
		if mov == "D":
			i += 1
		if mov == "A":
			y -= 1
		if mov == "B":
			y += 1
	if sm[y][i] == "B":
		print("Camino Hacia Bomba ---> *** " + camino + "***")
		ruta(sm, camino)
		return True

i = queue.Queue()
i.put("")
add = ""

while not final(sm,add): 
	add = i.get()
	for j in ["D -> ", "I -> ", "A -> ", "B -> "]:
		put = add + j
		if valida(sm, put):
			i.put(put)