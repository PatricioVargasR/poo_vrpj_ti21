"""
    Reto5
    Nombre: Patricio de Jesús Vargas Ramírez
    Fecha: 07/02/2023
    Descripción: Media de N números
"""

def calcular_media(numeros):
    suma = 0
    for numero in numeros:
        suma = suma + numero
    media = suma / len(numeros)
    return media

numeros = [1, 2, 3, 4, 5]
resultados = calcular_media(numeros)

print("La media aritmética es: {}" .format(resultados))