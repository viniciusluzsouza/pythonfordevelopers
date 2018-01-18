# -*- coding: latin-1 -*-
import os
from itertools import count

def ver_primo(num):

	if num == 0 or num ==1:
		return False

	for i in range(2,num/2):
		if not num % i:
			return False
		else:
			return True




primos = (i for i in count() if ver_primo(i))

for i in range(10):
	print primos.next()



