"""Escribe un programa que solicite una puntuación entre 0.0 y 1.0. Si la
puntuación está fuera de ese rango, muestra un mensaje de error."""
def calcula_puntuacion(puntuacion):
    print("Puntuación Calificación")
    if puntuacion >= 0.9 and puntuacion <= 1:
        print(">= 0.9     Sobresaliente")
    elif puntuacion <= 0.8:
        print(">= 0.8     Notable")
    elif puntuacion <= 0.7:
        print(">= 0.7     Bien")
    elif puntuacion <= 0.6:
        print(">= 0.6     Suficiente")  
    elif puntuacion < 0.6:
        print("< 0.6      Insuficiente")  
    else:
        print("La puntuacion esta fuera del rango establecido")

try:
    puntuacion = float(input("Introduzca una puntuación entre 0.0 y 1.0\n"))
except:
    print("Por favor introduzca, un numero.")

        
calcula_puntuacion(puntuacion)