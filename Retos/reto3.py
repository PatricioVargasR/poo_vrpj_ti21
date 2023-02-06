"""
    Reto2
    Nombre: Patricio de Jesús Vargas Ramírez
    Fecha: 04/02/2023
    Descripción: Minimo Común Multiplo
"""

numero1 = float(input("Ingresa tu primer número: "))
numero2 = float(input("Ingresa tu segundo número: "))

def maximo_comun_divisor(numero1, numero2):
    temporal = 0
    while numero2 != 0:
        temporal = numero2
        numero2 = numero1 % numero2
        numero1 = temporal
    return numero1

def minimo_comun_multiplo(numero1, numero2):
    return (numero1 * numero2) / maximo_comun_divisor(numero1, numero2)

mcm = minimo_comun_multiplo(numero1, numero2)
print(f"El mínimo común múltiplo de {numero1} y {numero2} es {mcm}")
