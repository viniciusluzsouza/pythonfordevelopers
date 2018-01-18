# -*- coding: latin-1 -*-
import os

class Square():

	def __init__(self, side):
		self.side = side

	def change_side(self, new_side):
		self.side = new_side

	def r_side(self):
		return self.side

	def area(self):
		return self.side * self.side

Quadrado = Square(4)

print "Lado:", Quadrado.r_side()
Quadrado.change_side(5)
print "Novo lado:", Quadrado.r_side()
print "Area:", Quadrado.area()

