# -*- coding: latin-1 -*-
import os

def gen_pares():
	"""
	Gera números pares indefinidamente ...
	"""
	i = 0
	while True:
		i += 2
		yield i

# Encontra arquivos recursivamente
def find(path='.'):
	for item in os.listdir(path):
		fn = os.path.normpath(os.path.join(path, item))
		if os.path.isdir(fn):
			for f in find(fn):
				yield f
		else:
			yield fn

# A cada iteração, o gerador devolve
# um novo nome de arquivo
for fn in find('/home/vini/python/umdir'):
	print fn
