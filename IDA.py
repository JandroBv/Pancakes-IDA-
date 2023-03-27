import random
import math

class Pancakes:

	def __init__(self, pancakes):
		self.pancakes = pancakes
		self.orden = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m","n", "o", "p", "q", "r", "s", "t", "u", "v","w", "x", "y", "z"]
		self.solucion = ""
	
	def voltear(self, posicion, pancakes):
		return pancakes[0:len(pancakes)-posicion] + pancakes[len(pancakes)-posicion:len(pancakes)][::-1]

	def h(self, nodo):
		c = 0
		if (nodo[0] != "a" and nodo[0] != "b"):
			c = 1
		for i in range(len(nodo)-1):
			if (abs(self.orden.index(nodo[i])-self.orden.index(nodo[i+1])) > 1):
				c += 1
		return c

	def ida(self, nodo):
		if nodo == self.orden[0:len(nodo)]:
			return 
		cota = self.h(nodo)
		while True:
			resultado = self.busqProfundidad(nodo, ["0"], cota)
			if resultado == True:
				return " ".join(self.solucion[1:])
			
			cota = resultado


	def busqProfundidad(self, nodo, ant, cota):

		f = self.h(nodo) + len(ant) - 1

		if f > cota:
			return  f

		if nodo == self.orden[0:len(nodo)]:
			return True
		
		minimo = math.inf 

		for i in range(2, len(nodo) + 1):
			if i == ant[-1]:
				continue
			nodo_volt = self.voltear(i, nodo)
			resultado = self.busqProfundidad(nodo_volt, ant + [str(i)], cota)
			if resultado == True:
				if self.solucion == "":
					self.solucion = ant + [str(i)]
				return True
			if resultado < minimo:
				minimo = resultado

		return minimo

pancakes = ["a", "b", "c", "d","e", "f","g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t","u", "v", "w", "x", "y", "z"]
random.shuffle(pancakes)
print(f"Pancakes inicio: {pancakes}")
prueba = Pancakes(pancakes)
print(f"Solucion: {prueba.ida(pancakes)}")
