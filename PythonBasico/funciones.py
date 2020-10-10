def funcion():
    return "Hola mundo"

frase = funcion()
print (frase)

def mi_funcion(nombre, apellido):
    nombre_completo = nombre, apellido
    print(nombre_completo)

mi_funcion("Rony", "Ortiz")

def saludar(nombre, mensaje='Hola'):

    print (mensaje, nombre)

saludar('Pepe el Grillo')

def recorrer_parametros_arbitrarios(parametro_fijo, *arbitrarios):
    print(parametro_fijo)
    # Los parámetros arbitrariso se corren como tuplas
    for argumento in arbitrarios:
        print(argumento)
    
recorrer_parametros_arbitrarios('Fixed', 'arbitrario 1', 'arbitrario 2', 'arbitrario 3')

