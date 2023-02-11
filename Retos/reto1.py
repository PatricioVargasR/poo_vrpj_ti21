"""
    Reto1
    Nombre: Patricio de Jesús Vargas Ramírez
    Fecha: 03/02/2023
    Descripción: Programa que verifica si un número es par o
    impar
"""
 
numero1 = float(input("Ingrese su número: "))  # Ingresa un dato del teclado
elevado = ((-1)**numero1)

if numero1 == 0:  # Si el valor ingresado es igual a 0
    print("Nulo") # Imprime la cadena "Nulo 
elif elevado > 0:  # En cambio, si la sentencia es falsa, evalua de nuevo
    print("Par")  # Imprime la cadena "Par"
else:   # Si ninguna de las anteriores se cumplió, ejecuta esta
    print("Impar")  # Imprime la cadena "Impar"
