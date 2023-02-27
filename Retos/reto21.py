"""
    Reto21
    Nombre: Patricio de Jesús Vargas Ramírez
    Fecha: 26/02/2023
    Descripción: ¿Cuántas veces aparece la letra a?
"""

oracion = str(input("Ingresa una oración: "))  # Ingresamos la oración

def cantidad(oracion):  # Definimos una función teniendo como parametros las variables anteriores

    oracion = oracion.lower()  # Hacemos todas las letras minusculas
    
    contador = 0  # Inicializamos una variable

    for caracter in oracion:  # Recorremos cada carácter de la oración 

        if caracter == "a":  # Si el carácter es igual a la letra a
            contador += 1  # Incrementamos en 1 el contador
    return contador  # Regresamos contador

cantidad_aparicion = cantidad(oracion)  # Pasamos el resultado de la función a una variable

print("La letra a, aparece {} en la oración ingresada" .format(cantidad_aparicion))  # Imprimimos el resultado
