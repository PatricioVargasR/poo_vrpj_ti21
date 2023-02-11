"""
    Reto5
    Nombre: Patricio de Jesús Vargas Ramírez
    Fecha: 07/02/2023
    Descripción: Media de N números
"""

def calcular_media(numeros):  # Declaramos una función con un parametro
    suma = 0  # Inicializamos una variable
    for numero in numeros:  # Iteramos en los numeros para sumarlos
        suma = suma + numero  # Sumanos cada numero y lo volvemos a almacenar
    media = suma / len(numeros)  # Dividimos por el total de los elementos
    return media  # Devolvemos el resultado de la media

numeros = [1, 2, 3, 4, 5]  # Definimos una lista de números
resultados = calcular_media(numeros)  # Almacenamos el resultado en una nueva variable

print("La media aritmética es: {}" .format(resultados))  # Imprimimos el resultado
