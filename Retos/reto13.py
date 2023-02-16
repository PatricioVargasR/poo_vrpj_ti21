"""
    Reto13
    Nombre: Patricio de Jesús Vargas Ramírez
    Fecha: 15/02/2023
    Descripción: ¿Cuántas veces sale la letra?
"""

oracion = str(input("Ingresa una oración: "))  # Ingresamos la oración
letra = input("Ingresa una letra: ")  # Ingresamos la letra

def cantidad(oracion, letra):  # Definimos una función teniendo como parametros las variables anteriores
    
    contador = 0  # Inicializamos una variable

    for caracter in oracion:  # Recorremos cada carácter de la oración 

        if caracter == letra:  # Si el carácter es igual a la letra ingresada
            contador += 1  # Incrementamos en 1 el contador
    return contador  # Regresamos contador

cantidad_aparicion = cantidad(oracion, letra)  # Pasamos el resultado de la función a una variable

print("La letra {}, aparece {} en la oración ingresada" .format(letra, cantidad_aparicion))  # Imprimimos el resultado