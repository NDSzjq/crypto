# -*- coding: utf-8 -*-

from Crypto.Hash import SHA256

block_size = 1024           # tamaño del bloque
''' El fichero se partira en bloques de tamaño block_size empezando desde el principio (el último bloque puede tener menos de 1024 bytes '''


#f = open('6 - 2 - Generic birthday attack (16 min).mp4', 'rb')      # abrir el fichero en modo lectura (b añadida para ficheros binarios en Windows)
f = open('6.1.intro.mp4_download', 'rb')      # abrir el fichero en modo lectura (b añadida para ficheros binarios en Windows)
f.seek(0,2)                 # (offset, mode) el mode 2 indica el final del fichero
size = f.tell()             # devuelve un entero con la posición del cursor en el fichero
last_block_size = size % block_size

lista = range(0,size, block_size)
lista.reverse()             # lista que incluye los índices del fichero partido en bloques de tamaño block_size

# Iterar sobre la lista e imprimir el hash del primero de los bloques
last_hash = ""
for l in lista:
    f.seek(l,0)
    block = f.read(block_size)
    h = SHA256.new()
    h.update(block)
    h.update(last_hash)
    last_hash = h.digest()

print last_hash.encode('hex')
