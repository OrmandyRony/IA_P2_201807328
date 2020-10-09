# -*- coding: utf-8 -*-
#Estructuras de control de flujo

#Asignación múltiple

a, b, c = 'string', 15, True

print (a)
print (b)
print (c)

# En una tupla 
mi_tupla = ('Hello world', 2020)
texto, anio = mi_tupla

print (texto)
print (anio)

# En una lista
mi_lista = ['Argentina', 'Buenos Aires']
pais, provincia = mi_lista

print (pais)
print (provincia)

# Estructuras de control de flujo condicionales

compra = 99

if compra <= 100:
    print("Pago en efectivo")
elif compra > 100 and compra < 300:
    print ("Pago con tarjeta de debito")
else:
    print ("Pago con tarjeta de crédito")

# Estructuras de control iterativas

#Bucle while
anio = 2001

while anio <=  2012:
    print("Informes del Año", str(anio))
    anio += 1

"""
while True:
    nombre = input("Indique su nombre")
    if nombre:
        break
"""

# Bucle for 

mi_lista = ['Juan', 'Antonio', 'Pedro', 'Dilan']
for nombre in mi_lista:
    print (nombre)
print()

mi_tupla = ('rosa', 'verde', 'amarillo')
for color in mi_tupla:
    print (color)

for anio in range(2001, 2013):
    print (anio)

for number in range(1, 11):
    print(number)

for i in [0, 1, 2]:
    print("cough")

for i in range(3):
    for j in range(3):
        print("#", end="")
    print()