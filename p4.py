# -*- coding: latin1 -*-

# # Função decoradora
# def dumpargs(f):

# 	# Função que envolverá a outra
# 	def func(*args):
# 		# Mostra os argumentos passados para a função
# 		print args
# 		# Retorna o resultado da função original
# 		return f(*args)
# 	# Retorna a função modificada
# 	return func

# @dumpargs
# def multiply(*nums):
# 	m = 1
	
# 	for n in nums:
# 		m = m * n
# 	return m

# print multiply(1, 2, 3)

class Cell(object):
	"""
	Classe para células de planilha
	"""
	def __init__(self, formula='""', format='%s'):
		"""Classes
		113
		Inicializa a célula
		"""
		self.formula = formula
		self.format = format
	def __repr__(self):
		"""
		Retorna a representação em string da célula
		"""
		return self.format % eval(self.formula)

print Cell('123**2')
print Cell('23*2+2')
print Cell('abs(-1.45 / 0.3)', '%2.3f')
