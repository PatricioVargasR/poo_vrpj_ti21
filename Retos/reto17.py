"""
    Reto17
    Nombre: Patricio de Jesús Vargas Ramírez
    Fecha: 19/02/2023
    Descripción: ¿Cuantas veces sale una palabra?
"""

oracion = str(input("Ingresa una oración: "))  # Ingresamos la oración
palabra = input("Ingresa la palabra a buscar: ")  # Ingresamos la letra

def cantidad(oracion, palabra):  # Definimos una función teniendo como parametros las variables anteriores
    
    contador = 0  # Inicializamos una variable
    oracion_nueva = oracion.lower().replace(","," ").split()  # Convertimos todo a minusculas, reemplazamos las comas por espacios y separamos las frases por esos espacios
    
    for caracter in oracion_nueva:  # Recorremos cada parte de la oración 
        if caracter == palabra:  # Si el carácter es igual a la palabra ingresada
            contador += 1  # Incrementamos en 1 el contador
    return contador  # Regresamos contador

cantidad_aparicion = cantidad(oracion, palabra)  # Pasamos el resultado de la función a una variable

print("La frase {} aparece {} veces en la oración ingresada" .format(palabra, cantidad_aparicion))  # Imprimimos el resultado