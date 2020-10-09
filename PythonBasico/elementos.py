# Variables
mi_variable = 12
MI_CONSTANTE = 12

print (mi_variable)

# Tipos de datos
mi_Cadena = "Hola Mundo!"

mi_cadena_multilinea = """
Esta es una cadena
de varias lineas
"""
# Numero entero
edad = 35

# Numero entero octal
# edad = 043

# Numero entero hexadecimal
edad = 0x23

# Numero real
precio = 7435.28

# Booleanao (verdadero/Falso)
verdadero = True
falso = False

# Operadores Aritmeticos

# Esto es un comentario

"""Y este es un comentario de 
varias lineas"""

"""Tipos de datos complejos"""

# Tuplas
""" Una tupla es una variable que permite almacenar varios datos inmutables
(no pueden ser modificados una vez creados) de tipos diferentes"""

print ("Resultados de tupla")
mi_tupla = ('cadena de texto', 15, 2.8, 'otro dato', 25)

print (mi_tupla[1]) # Salida 15

print (mi_tupla[1:4]) # Devuelve (15, 2.8, 'Otro dato')

print (mi_tupla[3:]) # Devuelve ('otro dato', 25)

print (mi_tupla[:2]) # Devuelve ('cadena de texto', 15)

# Listas 
""" Una lista es similar a una tupla con la diferencia fundamental de que permite
modificar los datos una vez creados"""

print("Resultados de mi lista")
mi_lista = ['cadena de texto', 15, 2.8, 'otro dato', 25]

print (mi_lista[1]) # Salida: 15

print (mi_lista[1:4]) # Devuelve: [15, 2.8, 'otro dato'] 

print (mi_lista[-2]) # Salida: otro dato

"""Las lista No son inmutables: permiten modificar los datos una vez creados"""

mi_lista[2] = 3.8 # el tercer elemento ahota es 3.8

# Las listas, a diferencia de las tuplas, permiten agregar nuevos valores

mi_lista.append('Nuevo Dato')

print("Lista modificada", mi_lista[0:6])

# Diccionarios
"""Mientras que a las listas y tuplas se accede solo y únicamente por un número
de índice, los diccionarios permiten utilizar una clave para declarar y acceder
a un valor"""

mi_diccionario = {'clave_1': 'valor_1', 'clave_2': 'valor_2', 'clave_7': 'valor_7'}
print (mi_diccionario['clave_2']) # Salida: valor_2

# Un diccionario permite eliminar cualquier entrada
del(mi_diccionario['clave_2'])

# Al igual que las listas, el diccionario permite modificar los valores

mi_diccionario['clave_1'] = 'Nuevo Valor'

