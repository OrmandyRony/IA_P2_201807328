""" Escribe un programa para pedirle al usuario el número de
horas y la tarifa por hora para calcular el salario bruto. """

horas = float(input("Introduzca Horas:  "))
tarifa = float(input("Introduzca Tarifa:  "))
salario = horas * tarifa
print(f"Salario: {salario}")
