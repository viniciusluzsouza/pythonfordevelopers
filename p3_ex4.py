# -*- coding: latin-1 -*-
import os

def leArq(arquivo):
	try:
		dados = []

		arq = open(arquivo)

		for line in arq:
			line = line.strip()
			if len(line):
				linha = line.split(',')
				dados.append(tuple(linha))
				yield dados

		arq.close()

	except:
		print "Erro ao abrir o arquivo", arquivo
		raise SystemExit


for linha in leArq("planilha.csv"):
	print linha.pop()




