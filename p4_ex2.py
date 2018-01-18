# -*- coding: latin-1 -*-
import os

class Lista(object):

	def __init__(self):
		self.lista = list()

	def remove(self):
		return self.lista.pop()

	def adiciona(self, valor):
		self.lista.append(valor)

	def existe(self, listagem, valor):
		for elemento in listagem:
			if elemento == valor:
				return True
		return False

	def exibe(self):
		print self.lista



class OutraLista(Lista):
	def __init__(self):
		self.lista = list()

	def retorna_especial(self):
		novaLista = list()
		for elemento in self.lista:
			for element in novaLista:
				if element == elemento:
					break;
			else:
				novaLista.append(elemento);

		return novaLista


umaLista = OutraLista()
umaLista.adiciona(5)
umaLista.adiciona(4)
umaLista.adiciona(3)
umaLista.adiciona(2)
umaLista.adiciona(1)
umaLista.adiciona(0)

print "Primeira lista:", umaLista.exibe()


umaLista.adiciona(5)
umaLista.adiciona(4)
umaLista.adiciona(3)
umaLista.adiciona(2)
umaLista.adiciona(1)
umaLista.adiciona(0)

print "Segunda lista:", umaLista.exibe()

terceiraLista = umaLista.retorna_especial()

print "Terceira lista:", terceiraLista



