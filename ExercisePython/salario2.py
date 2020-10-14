"""Reescribe el programa del cálculo del salario para darle al empleado
1.5 veces la tarifa horaria para todas las horas trabajadas que excedan de 40."""
"""Reescribe el programa de cálculo del salario, con tarifa-ymedia
para las horas extras, y crea una función llamada calculo_salario
que reciba dos parámetros (horas y tarifa)."""

def calculo_salario(horas, tarifa):
    salario = 1.5*horas*tarifa
    return salario

try:
    horas = float(input("Introduzca la Horas: "))
    tarifa = float(input("Introduzca la Tarifa:"))
    salario = calculo_salario(horas, tarifa)

    print("Salario: ", salario)

except:
    print('Error, por favor introduzca un número')