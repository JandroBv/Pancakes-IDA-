import random
import math

class Pancakes:

	def __init__(self, pancakes):
		self.pancakes = pancakes
		self.orden = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m","n", "o", "p", "q", "r", "s", "t", "u", "v","w", "x", "y", "z"]
		self.profundidad = 1
		self.valor = self.h(pancakes)
		self.min = math.inf
		self.cota = self.valor
	
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
		while True:
			resultado = self.busqProfundidad(nodo, ["0"], self.h(nodo))
			if resultado == -1:
				self.profundidad += 1
			elif resultado == -2:
				self.cota = self.min
				self.min = math.inf
			else:
				return resultado

	def busqProfundidad(self, nodo, ant, h):
		if nodo == self.orden[0:len(nodo)]:
			return " ".join(ant[1:])
	
		if len(ant)-1 >= self.profundidad:
			return -1 
		for i in range(2, len(nodo)+1):
			if str(i) == ant[-1]:
				continue 
			nodo_volt = self.voltear(i,nodo)
			if (self.h(nodo_volt) + 1) <= self.cota:
					resultado = self.busqProfundidad(nodo_volt, ant + [str(i)], self.h(nodo_volt))
					if resultado != -1:
						break
			else:
				if (self.h(nodo_volt) + 1) < self.min:
					self.min = self.h(nodo_volt) + 1
				resultado = -2
		return resultado


pancakes = ["a", "b", "c", "d","e", "f"]
random.shuffle(pancakes)
print(f"Pancakes inicio: {pancakes}")
prueba = Pancakes(pancakes)
print(prueba.ida(pancakes))
