"""
    Reto1
    Nombre: Patricio de Jesús Vargas Ramírez
    Fecha: 03/02/2023
    Descripción: Programa que verifica si un número es par o
    impar
"""

numero1=int(input("Ingrese su número"))  # Ingresa un dato del teclado

elevacion = (-1**numero1)  # Utilizando el dato ingresado eleva un valor

if numero1 == 0:  # Si el valor ingresado es igual a 0
    print("Nulo") # Imprime la cadena "Nulo"
elif numero1 == elevacion>0:  # En cambio, si la sentencia es falsa, evalua de nuevo
    print("Par")  # Imprime la cadena "Par"
else:   # Si ninguna de las anteriores se cumplió, ejecuta esta
    print("Impar")  # Imprime la cadena "Impar"
