"""
    Programa 3
    Nombre: Patricio de Jesús Vargas Ramírez
    Fecha: 24/01/2023
    Descripción: Usar print con operaciones
    aritméticas(format)
"""

numero1 = 10  # Variable de tipo int
numero2 = 5  # Variable de tipo int

print("{} + {} = ".format(numero1, numero2), (numero1 + numero2))  # 10 + 5 = 15

print((numero1 * numero2), "= {} * {} ".format(numero1, numero2))  # 50 = 5 * 10

print("{} = {} * {}".format((numero1 * numero2), numero1, numero2))  # 50 = 5 * 10

print("El resultado de dividir {} / {} es".format(numero1, numero2), (numero1 / numero2))  # El resultado de dividr 10 / 5 es 2

#suma = numero1+numero2  # Suma dos numeros
#print("{} + {} =" .format(numero1, numero2),suma)  # Imprime con format
#print(numero1 + numero2)  # 15
#print("{}+{}" .format(numero1, numero2))  # 10+5
#print("{}{}" .format(numero1, numero2))  # Imprime dos valores con el format
