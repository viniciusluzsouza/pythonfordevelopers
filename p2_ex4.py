# -*- coding: latin1 -*-
import sys
import os.path
import string

def split(fn, n):

	bytes = list(file(fn, 'rb').read())
	name, ext = fn.split('.')
	num = 1
	while bytes:
		out = ''.join(bytes[:n])
		del bytes[:n]
		newfn = '%s_%3d.%s' % (name, num, ext)
		file(newfn, 'wb').write(out)
		num += 1

# Junta as fatias em um arquivo
def join(fn, fnlist):
	out = ''
	for f in fnlist:
		out += file(f, 'rb').read()
	file(fn, 'wb').write(out)


if __name__ == '__main__':
	# Teste
	import glob
	split('breaker.py', 20)
	join('breaker2.py', sorted(glob.glob('breaker_*.py')))

