# -*- coding: latin1 -*-
# importando o módulo string
import string


instrumentos = ['baixo','bateria','guitarra']

for instrumento in instrumentos:
	print instrumento





for i in [234, 654, 378, 798]:
	if i % 3 == 0:
		print i, '/ 3 =', i/3



# temp = int(raw_input('Entre com a temperatura:'))

# if temp < 0:
# 	print 'Congelando ...'
# elif 0 <= temp <= 20:
# 	print 'Frio'
# elif 21 <= temp <= 25:
# 	print 'Normal'
# elif 26 <= temp <= 35:
# 	print 'Quente'
# else:
# 	print 'Muito quente!'

#real para inteiro
print 'int(3.14) =', int(3.14)

#inteiro para real
print 'float(5) =', float(5)

#calculo entre inteiro e real resulta em real
print '5.0 / 2 + 3 =', 5.0 / 2 + 3

#inteiros em outra base
print "int('20',8) =", int('20', 8) #base 8
print "int('20', 16) =", int('20', 16) #base 16

#operacoes com numeros complexos
c = 3 + 4j
print 'c =', c
print 'Parte real:', c.real
print 'Parte imaginaria:', c.imag
print 'Conjugado:', c.conjugate()

print '(3+4j) + (5+6j) =', c + (5+6j)


s = 'Camel'
# Concatenação
print 'The ' + s + ' run away!'
# Interpolação
print 'tamanho de %s => %d' % (s, len(s))
# String tratada como sequência
for ch in s: print ch
# Strings são objetos
if s.startswith('C'): print s.upper()
# o que acontecerá?
print 3 * s
# 3 * s é consistente com s + s + s

# Zeros a esquerda
print 'Agora são %02d:%02d.' % (16, 30)
# Real (número após o ponto controla as casas decimais)
print 'Percentagem: %.1f%%, Exponencial:%.2e' % (5.333, 0.00314)
# Octal e hexadecimal
print 'Decimal: %d, Octal: %o, Hexadecimal: %x' % (10, 10, 10)


# musicos = [('Page', 'guitarrista', 'Led Zeppelin'),
# ('Fripp', 'guitarrista', 'King Crimson')]
# # Parâmetros identificados pela ordem
# msg = '{0} é {1} do {2}'
# for nome, funcao, banda in musicos:
# print(msg.format(nome, funcao, banda))
# # Parâmetros identificados pelo nome
# msg = '{saudacao}, são {hora:02d}:{minuto:02d}'
# print msg.format(saudacao='Bom dia', hora=7, minuto=30)
# # Função builtin format()
# print 'Pi =', format(3.14159, '.3e')

# Mostra: nohtyP
print 'Python'[::]


# Cria uma string template
st = string.Template('$aviso aconteceu em $quando')
# Preenche o modelo com um dicionário
s = st.substitute({'aviso': 'Falta de eletricidade',
'quando': '03 de Abril de 2002'})
# Mostra:
# Falta de eletricidade aconteceu em 03 de Abril de 2002
print s


# Uma nova lista: Brit Progs dos anos 70
progs = ['Yes', 'Genesis', 'Pink Floyd', 'ELP']
# Varrendo a lista inteira
for prog in progs:
	print prog
# Trocando o último elemento
progs[-1] = 'King Crimson'
# Incluindo
progs.append('Camel')
# Removendo
progs.remove('Pink Floyd')
# Ordena a lista
progs.sort()
# Inverte a lista
progs.reverse()
# Imprime numerado
for i, prog in enumerate(progs):
	print i + 1, '=>', prog
# Imprime do segundo item em diante
print progs[1:]


lista = ['A', 'B', 'C']
print 'lista:', lista
# A lista vazia é avaliada como falsa
while lista:
# Em filas, o primeiro item é o primeiro a sair
# pop(0) remove e retorna o primeiro item
	print 'Saiu', lista.pop(0), ', faltam', len(lista)
# Mais itens na lista
lista += ['D', 'E', 'F']
print 'lista:', lista
while lista:
# Em pilhas, o primeiro item é o último a sair
# pop() remove e retorna o último item
	print 'Saiu', lista.pop(), ', faltam', len(lista)

# Conjuntos de dados
s1 = set(range(3))
s2 = set(range(10, 7, -1))
s3 = set(range(2, 10, 2))
# Exibe os dados
print 's1:', s1, '\ns2:', s2, '\ns3:', s3
# União
s1s2 = s1.union(s2)
print 'União de s1 e s2:', s1s2
# Diferença
print 'Diferença com s3:', s1s2.difference(s3)
# Interseção
print 'Interseção com s3:', s1s2.intersection(s3)
# Testa se um set inclui outro
if s1.issuperset([1, 2]):
	print 's1 inclui 1 e 2'
# Testa se não existe elementos em comum
if s1.isdisjoint(s2):
	print 's1 e s2 não tem elementos em comum'


# Progs e seus albuns
progs = {'Yes': ['Close To The Edge', 'Fragile'],
'Genesis': ['Foxtrot', 'The Nursery Crime'],
'ELP': ['Brain Salad Surgery']}
# Mais progs
progs['King Crimson'] = ['Red', 'Discipline']
# items() retorna uma lista de
# tuplas com a chave e o valor
for prog, albuns in progs.items():
	print prog, '=>', albuns
# Se tiver 'ELP', deleta
if progs.has_key('ELP'):
	del progs['ELP']




dim = 6, 12
mat = {}
# Tuplas são imutáveis
# Cada tupla representa
# uma posição na matriz
mat[3, 7] = 3
mat[4, 6] = 5
mat[6, 3] = 7
mat[5, 4] = 6
mat[2, 9] = 4
mat[1, 0] = 9
for lin in range(dim[0]):
	for col in range(dim[1]):
	# Método get(chave, valor)
	# retorna o valor da chave
	# no dicionário ou se a chave
	# não existir, retorna o
	# segundo argumento
		print mat.get((lin,col), 0),
	print








