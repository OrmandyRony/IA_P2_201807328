""" Escribe un programa que le pida al usuario una temperatura
en grados Celsius, la convierta a grados Fahrenheit e imprima
por pantalla la temperatura convertida. """
print("Convertidor de grados celcius a fahrenheit")
celcius = float(input("Ingrese los grados celcius: "))
fahrenheit = (celcius * 9/5) + 32
print("Grados farenheit: ", fahrenheit)