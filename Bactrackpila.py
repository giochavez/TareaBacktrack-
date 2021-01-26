class Vertice: #representa cada vértice del grafo
    def __init__(self,clave): #self es como poner una declaración en C, para no tener que poner un mismo nombre
        self.id = clave
        self.conectadoA = {}

    def agregarVecino(self,vecino,ponderacion=0): #agregar conexion de un vertice a otro
        self.conectadoA[vecino] = ponderacion

    def __str__(self): #imprimimos el grafo y sus conecciones 
        return str(self.id) + ' conectadoA: ' + str([x.id for x in self.conectadoA])

    def obtenerConexiones(self): #devuelve todos los vertices de la lista
        return self.conectadoA.keys()

    def obtenerId(self): #obtenemos el nombre del vertice
        return self.id

    def obtenerPonderacion(self,vecino): #obtenemos al vertice al cual se esta conectado
        return self.conectadoA[vecino]
        
class Grafo: #listas maestras de vértices
    def __init__(self):
        self.listaVertices = {}
        self.numVertices = 0

    def agregarVertice(self,clave): #agregamos vertice (aun no se ocupa)
        self.numVertices = self.numVertices + 1
        nuevoVertice = Vertice(clave)
        self.listaVertices[clave] = nuevoVertice
        return nuevoVertice

    def obtenerVertice(self,n): #devuelve los nombres de todos los vértices del grafo
        if n in self.listaVertices:
            return self.listaVertices[n]
        else:
            return None

    def __contains__(self,n):
        return n in self.listaVertices

    #def agregarArista(self,de,a,costo=0):
    def agregarArista(self,de,a): #si
        if de not in self.listaVertices:
            nv = self.agregarVertice(de)
        if a not in self.listaVertices:
            nv = self.agregarVertice(a)
        #self.listaVertices[de].agregarVecino(self.listaVertices[a], costo)
        self.listaVertices[de].agregarVecino(self.listaVertices[a])

    def obtenerVertices(self):
        return self.listaVertices.keys()

    def __iter__(self): #facilitar la iteracion sobre todos los objetos vértice de un grafo en particular 
        return iter(self.listaVertices.values())

def Vacia (Pila):
    return len(Pila)== 0
def nodoSiguiente(nodoActual,Recorrido,Cerrados):
    abiertos=[]
    for llave,valor in nodoActual.items():
        if((valor !=0) and (llave not in Recorrido) and (llave not in Cerrados)):
            abiertos.append(valor)
    if(len(abiertos)==0):
        return False
    else:
        menor=abiertos[0]
        for x in abiertos:
            if(menor>x):
                menor=x
        for llave,valor in nodoActual.items():
            if(valor==menor):
                return llave
def backtrack(grafo,inicio,final):
    Recorrido=[]
    Cerrados=[]
    nodoactual=inicio
    Recorrido.append(nodoactual)
    while True:
        nodoactual=nodoSiguiente(grafo[nodoactual],Recorrido,Cerrados)
        if(nodoactual==final):
            Recorrido.append(final)
            return Recorrido
        if(nodoactual==False):
            aux=Recorrido.pop()
            Cerrados.append(aux)
            nodoactual=Recorrido[-1]
        else:
            Recorrido.append(nodoactual)
    
if __name__=="__main__":

    g = Grafo()
    g.agregarArista('A','B')
    g.agregarArista('A','C')
    g.agregarArista('A','D')
    g.agregarArista('A','F')
    g.agregarArista('B','E')
    g.agregarArista('C','E')
    g.agregarArista('D','G')
    g.agregarArista('D','I')
    g.agregarArista('E','F')
    g.agregarArista('G','H')
    g.agregarArista('I','H')
    print("Grafo representado como grafo:\n")
    for v in g:
        for w in v.obtenerConexiones():
            print("(%s,%s)"%(v.obtenerId(), w.obtenerId()))
    print("\nConexiones:")
    for a in g:
        print(a.__str__())
    
    grafo={
        "A":dict(zip('ABCDEFGHI',[0,20,30,100,0,50,0,0,0])),
        "B":dict(zip('ABCDEFGHI',[0,0,0,0,19,0,0,0,0])),
        "C":dict(zip('ABCDEFGHI',[0,0,0,0,23,0,0,0,0])),
        "D":dict(zip('ABCDEFGHI',[0,0,0,0,0,0,20,0,70])),
        "E":dict(zip('ABCDEFGHI',[0,0,0,0,0,42,0,0,0])),
        "F":dict(zip('ABCDEFGHI',[0,0,0,0,0,0,0,0,0])),
        "G":dict(zip('ABCDEFGHI',[0,0,0,0,0,0,0,16,0])),
        "H":dict(zip('ABCDEFGHI',[0,0,0,0,0,0,0,0,0])),
        "I":dict(zip('ABCDEFGHI',[0,0,0,0,0,0,0,0,65]))
    }
    fin = input("Nodo término (MAYÚSCULA)? ")
    print("\nSolución:")
    prueba=backtrack(grafo,"A",fin)
    print(prueba)
