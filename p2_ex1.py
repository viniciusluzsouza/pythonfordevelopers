# -*- coding: latin1 -*-
import sys
import os.path
import string

# Exercicio 1
arquivo = raw_input("Entre com o nome do arquivo: ")
arq = open(arquivo)

c, w, l = 0, 0, 0
for line in arq:
	l += 1
	c += len(line)
	w += len(line.split())

arq.close()

print 'Bytes: %d, Palavras: %d, Linhas: %s' % (c, w, l)



