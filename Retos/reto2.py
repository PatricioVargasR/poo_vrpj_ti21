"""
    Reto2
    Nombre: Patricio de Jesús Vargas Ramírez
    Fecha: 04/02/2023
    Descripción: Programa que pasa de grados Celsius a
    Fahrenheit
"""
grados = float(input("Ingresa los grados en Celisus: "))  # Ingresamos un valor del teclado

constante = 1.8  # Declaramos una constante 
fahrenheit = (grados * constante) + 32    # Operamos los grados con una formular

print("{} grados Celsius son iguales a {} grados fahrenheit" .format(grados, fahrenheit))  # Imprimimos el resultado
