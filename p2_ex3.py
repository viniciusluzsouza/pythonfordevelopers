# -*- coding: latin1 -*-
import sys
import os.path
import string

def LeArq(arquivo):
	try:
		dados = []

		arq = open(arquivo)

		for line in arq:
			line = line.strip()
			if len(line):
				linha = line.split(',')
				print linha
				umDado = tuple(linha)
				dados.append(umDado)

		arq.close()

		return dados
	except:
		print "Ocorreu um erro!!"
		raise SystemExit

retorno = LeArq("planilha.csv")
print retorno
