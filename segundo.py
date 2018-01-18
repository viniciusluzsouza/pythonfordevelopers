import sys
import os
import glob

# temp = open('temp.txt', 'w')

# for i in range (100):
# 	temp.write('%03d\n' % i)

# temp.close()

# temp = open('temp.txt', 'r')

# for x in temp:
# 	sys.stdout.write(x)

# temp.close()

# fn = raw_input('Nome do arquivo: ').strip()

# if not os.path.exists(fn):
# 	print 'Tente outra vez ...'
# 	sys.exit()

# for i,s in enumerate(open(fn)):
# 	print i + 1,s,

#print open('temp.txt').readlines()

for arq in sorted(glob.glob('*.py')):
	print 'Arquivo:', arq, '| Tamanho:', os.path.getsize(arq)

texto = 'Teste'
temp = os.tmpfile()
temp.write(texto)
temp.seek(0)
print temp.read()
temp.write('Teste 2')
print temp.read()
temp.close()





