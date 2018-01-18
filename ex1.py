# -*- coding: latin1 -*-

#exercicio 1
def FahreCelsius(grau):
	return (5*(grau - 32)) / 9

def CelsiusFahre(grau):
	return ((9*grau)/5) + 32

#print 'Temperatura convertida: %.02f' % FahreCelsius(90)

#exercicio 2
def VerPrimo(num):

	if (num < 2): return 0
	for i in range(2,(num/2)):
		if ( (num % i) == 0 ): return 0

	return 1

# n=5
# if VerPrimo(n):
# 	print 'O numero e primo'
# else:
# 	print 'O numero nao e primo'

#exercicio 4
def VerHash(dicionario):
	valores = dicionario.values()

	soma = 0
	for valor in valores:
		soma = soma + valor

	media = float(soma) / len(valores)
	resultado = [soma, media]
	return resultado

# dic1 = {'a':1, 'b':2, 'c':3, 'd':4, 'e':5, 'f':6}
# print VerHash(dic1)

#exercicio 5
def InverteFrase(frase):
	return frase[::-1]

# umaFrase = "Esta frase sera invertida"
# print "Frase a inverter:", umaFrase
# print "Frase invertida:", InverteFrase(umaFrase)

