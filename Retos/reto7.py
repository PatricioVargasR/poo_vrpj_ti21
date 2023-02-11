"""
    Reto7
    Nombre: Patricio de Jesús Vargas Ramírez
    Fecha: 09/02/2023
    Descripción: Ordenar números de forma descendentes
"""

numero1 = float(input("Numero 1: "))  # Se pide un valor al usuario
numero2 = float(input("Numero 2: "))  # Se pide un valor al usuario
numero3 = float(input("Numero 3: "))  # Se pide un valor al usuario

if numero1 > numero2:  # Se busca que numero1 sea el mayor
    if numero1 > numero3:  # Se busca que numero1 seal el mayor entre los tres
        if numero2 > numero3:  # Se busca que numero2 sea mayor que numero3
            print(numero1, numero2, numero3)  # Imprime el resultado de forma descendente
        else:  # Si no se cumple una condición
            print(numero1, numero3, numero2)   # Imprime el resultado cambiando un lugar
    else:  # Si no se cumple la condición
        print(numero3, numero1, numero2)  # Imprime el resultado volviendo a cambiar el orden
elif numero2 > numero3:  # Se busca que numero2 sea mayor
    if numero1 > numero3:  # Se busca que numero1 sea mayor
        print(numero2, numero1, numero3)  # Se imprime el resultado a partir de la primera comparación
    else:  # Si no se cumple la condición
        print(numero2, numero3, numero1)  # El resultado se cambia a partir del segundo lugar
else:  # Si no se cumple la condición
    print(numero3, numero2, numero1)  # Cambia el resultado 
