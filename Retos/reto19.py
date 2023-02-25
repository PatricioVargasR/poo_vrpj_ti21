"""
    Reto19
    Nombre: Patricio de Jesús Vargas Ramírez
    Fecha: 23/02/2023
    Descripción: Mostrando las tablas de multiplicar a partir de una en especifico
"""

numero = int(input("Ingresa el numero de tablas que quiers ver: "))  # Pedimos un número 
numero += 1  # Incrementamos en uno el valor ingresado

def tablas_multiplicar(numero:int) -> int and str:  # Definimos una función tomando como valor el numero incrementado

    for i in range(1,numero):  # Para el valor i en el rango de 1 al valor ingresado
        print("Tabla del {}" .format(i))  # Imprimimos el mensaje

        for j in range(1,11):  # Pra el valor j en el rango de 1 a 11  
            multplicar = i * j  # Realizamos la multiplicación de i por j
            print("{} * {} = {}" .format(i, j, multplicar))  # Imprimimos esa multiplicación

tablas_multiplicar(numero)  # Llamamos a la función