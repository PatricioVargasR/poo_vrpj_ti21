"""
    Programa 8
    Nombre: Patricio de Jesús Vargas Ramírez
    Fecha: 02/02/2023
    Descripción: 
"""

numero1 = int(input("Ingresa un número: ")) # Pide un valor en el teclado
numero2 = int(input("Ingresa tu segundo número: ")) # Pide un valor en el teclado

if numero1 == numero2: # Se compara las dos entradas
    print(None)  # Imprime None si es verdadero
elif numero1 > numero2:  # Se compara otra vez en caso de ser falso
    print(numero1)  # Imprime numero1 si es verdadero
else:
    print(numero2)  # Imprime numero2 si es verdadero
