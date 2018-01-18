# -*- coding: latin1 -*-
import sys
import os.path
import string

def matrix_sum(*matrices):
	"""
	Soma matrizes de duas dimensões.
	"""
	# Pegue a primeira matriz
	mat = matrices[0]

	# Para cada matriz da segunda em diante
	for matrix in matrices[1:]:
		# Para cada linha da matriz
		for x, row in enumerate(matrix):
			# Para cada elemento da linha
			for y, col in enumerate(row):
				# Some na matriz de resposta
				mat[x][y] += col

	return mat

def camel_case(s):
	"""
	Formata strings DestaForma.
	"""
	return ''.join(s.title().split())


if __name__ == '__main__':

	# Testes
	print matrix_sum([[1, 2], [3, 4]], [[5, 6], [7, 8]])
	print camel_case('close to the edge')