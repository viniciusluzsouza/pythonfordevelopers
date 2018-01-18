# -*- coding: latin-1 -*-
import os
import time

def func_range():
	rgb = []

	for r in range(256):
		for g in range(256):
			for b in range(256):
				rgb.append((r,g,b))

	return rgb


def gerador_xrange():

	for r in xrange(256):
		for g in xrange(256):
			for b in xrange(256):
				yield (r,g,b)

tt = time.time()
l = func_range()
print time.time() - tt

tt = time.time()
for cor in gerador_xrange(): pass
print time.time() - tt




