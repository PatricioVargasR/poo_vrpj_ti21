"""
    Reto4
    Nombre: Patricio de Jesús Vargas Ramírez
    Fecha: 06/02/2023
    Descripción: Factorial de un número
"""

numero1 = float(input("Ingrese un número mayor a 0: "))  # Se pide un valor desde el teclado

if numero1 < 0:  # Verifica si el valor ingresado sea menor a cero
    print("Error: Número menor a 0.")  # Si es verdadero imprime un mensaje 
else:  # En cambio, si es falso
    n = 1  # Se inicializa una variable
    x = 1  # Se inicializa una variable
    while x <= numero1:  # Mientras x sea menor o igual a numero1 seguira operando
        n = n * x  # Se multiplica n por x para aumentar el valor de n
        x = x + 1  # Se va sumando 1 a x para alcanzar a numero1
    print("Factorial de {} es: {}" .format(numero1, n))  # Se imprime el factorial
    