"""
    Reto7
    Nombre: Patricio de Jesús Vargas Ramírez
    Fecha: 10/02/2023
    Descripción: Rangos con saltos
"""

numero1 = int(input("Ingrese su primer número: "))  # Se pide un valor
numero2 = int(input("Ingrese su segundo número: "))  # Se pide un valor
salto = int(input("Ingrese su salto: "))  # Se pide la secuencia

if salto != 0:  # Se compara que la secuencia sea diferente a cero
    lista = list(range(numero1, numero2, salto))  # Se crea una variable que toma el rango de los dos números dentro de una lista con un salto
else:  # En cambio, si es falsa
    lista = list(range(numero1, numero2))  # Se crea una variable que toma el rango de los dos números dentro de una lista sin salto

print(lista)  # Se imprime la lista
