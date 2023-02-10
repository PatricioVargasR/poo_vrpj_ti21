"""
    Reto7
    Nombre: Patricio de Jesús Vargas Ramírez
    Fecha: 09/02/2023
    Descripción: Ordenar números de forma descendentes
"""

numero1 = float(input("Numero 1: "))
numero2 = float(input("Numero 2: "))
numero3 = float(input("Numero 3: "))

def descendente(numero1:float, numero2:float, numero3:float) -> float and int and None:   
    resultado = None  
    if numero1 > numero2:
        if numero1 > numero3:
            if numero2 > numero3:
               resultado = numero1, numero2, numero3
            else:
                resultado = numero1, numero3, numero2
        else:
            resultado = numero3, numero1, numero2
    elif numero2 > numero3:
        if numero1 > numero3:
            resultado = numero2, numero1, numero3
        else:
            resultado = numero2, numero3, numero1
    else:
        resultado = numero3, numero2, numero1
    return resultado

descender = descendente (numero1, numero2, numero3)

print(descender)
