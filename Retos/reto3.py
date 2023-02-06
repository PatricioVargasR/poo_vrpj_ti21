"""
    Reto3
    Nombre: Patricio de Jesús Vargas Ramírez
    Fecha: 05/02/2023
    Descripción: Minimo Común Multiplo
"""

numero1 = float(input("Ingresa tu primer número: "))  # Se pide un valor desde el teclado
numero2 = float(input("Ingresa tu segundo número: "))  # Se pide un valor desde el teclado

def maximo_comun_divisor(numero1, numero2):  # Se crea una función que toma dos parametros
    temporal = 0  # Se inicializa una variable
    while numero2 != 0:  # Mientras numero2 sea diferente que 0
        temporal = numero2  # La variable tomará los valores de numero2
        numero2 = numero1 % numero2  # Numero2 obtendrá el residuo entre numero1 y numero2
        numero1 = temporal  # Numero1 obtendrá el valor de temporal
    return numero1  #  Se retorna el valor de numero1

def minimo_comun_multiplo(numero1, numero2):  # Se crea una función con dos parametros
    return (numero1 * numero2) / maximo_comun_divisor(numero1, numero2)  # Retorna el valor de numero1*numero2 entre la función mcd

mcm = minimo_comun_multiplo(numero1, numero2)  # Se asigna el valor de mcm con los parametros de mcm
print(f"El mínimo común múltiplo de {numero1} y {numero2} es {mcm}")  # Se imprime el valor de mcm