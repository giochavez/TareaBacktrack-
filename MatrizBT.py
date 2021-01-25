def movimiento(matriz,cerrados,camino): #diga la matriz, el nodo y los que estan cerrados al igual que el camino
	actual = camino[-1]#indices como números
	for k in matriz[actual]:
		if k != -1 and (if not k in camino) and (not k in cerrados):
			#posible paso siguiente
			#if not k in camino and not k in cerrados:
			return k
		#no hay ningun movimiento
	return -1

def backtrack(matriz,cerrados,camino,destino):
	pos_actual = camino[-1]
	while pos_actual != destino:
		#busqueda por backtrack
		siguiente = movimiento(matriz,cerrados,camino)
		if siguiente == -1:
			cerrados.append(pos_actual)
			camino.pop()
			if len(camino) == 0:
				return []
			pos_actual=camino[-1]
		else:
			camino.append(siguiente)
			pos_actual = siguiente



def main():
	nodo=list('abcdefkh')
	matriz =  [[-1, 1, 2, 4,-1,-1,-1,-1],
              [-1,-1,-1,-1,-1,-1, 1,-1],
              [-1,-1,-1,-1,-1, -1, 4,-1],
              [-1,-1,-1,-1, 1, 1,-1,-1],
              [-1,-1, 2,-1,-1,-1,-1, 1],
              [-1,-1,-1,-1,-1,-1,-1, 2],
              [-1,-1,-1,-1,-1,-1,-1, 1]
              ]

	cerrados = []
	camino = ['a']
	backtrack(matriz,cerrados,camino,nodo.index('h'))
