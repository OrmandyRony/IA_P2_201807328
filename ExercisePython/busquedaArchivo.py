# Búsqueda atravez de un archivo
man_a = open('mbox-short.txt')
contador = 0
for linea in man_a:
    linea = linea.rstrip()
    if linea.startswith('From:'):
        print(linea)
        