# -*- coding: latin1 -*-
import zipfile

"""
Gravando texto em um arquivo compactado
"""

texto = """
********************************************
Esse é o texto que será compactado e ....
.... guardado dentro de um arquivo .zip.
********************************************
"""

#Cria um novo zip
zip = zipfile.ZipFile('arq.zip', 'w', zipfile.ZIP_DEFLATED)

# Escreve uma string no zip como se fosse um arquivo
zip.writestr('texto.txt', texto)

# Fecha o ZIP
zip.close()

### Agora vamos ler o arquivo ....

#Abre o arquivo para leitura
zip_ler = zipfile.ZipFile('arq.zip')

# Pega a lista de arquivos compactados
arqs = zip_ler.namelist()

for arq in arqs:
	print 'Arquivo:', arq

	# Pegando informações do arquivo
	zipinfo = zip.getinfo(arq)
	print 'Tamanho original:', zipinfo.file_size
	print 'Tamanho comprimido:', zipinfo.compress_size

	# Mostra o conteudo do arquivo
	print zip_ler.read(arq)
	
zip_ler.close()

