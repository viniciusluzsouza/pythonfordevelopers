# -*- coding: latin-1 -*-
import os


def ver_primo(num):

	if num == 0 or num ==1:
		return False

	for i in range(2,num/2):
		if (num % i) == 0:
			return False

	return True

def gera_primos():

	n = 0

	while True:
		n += 1
		if ver_primo(n):
			yield n


# for z in range (1,50):
# 	if ver_primo(z):
# 		print z

for z in gera_primos():
	if z >= 1000: break
	print z

