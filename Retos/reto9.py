"""
    Reto9
    Nombre: Patricio de Jesús Vargas Ramírez
    Fecha: 11/02/2023
    Descripción: Sumar sin sumar
"""

numero1 = float(input("Ingrese su primer número: "))  # Pide un valor desde el teclado
numero2 = float(input("Ingrese su segundo número: "))  # Pide un valor desde el teclado

def suma(numero1, numero2) -> float:  # Creamos una función con dos parametros y que devolvera un flotante

    if numero1 > 0:  # Se busca que numero1 sea mayor a 0
        while numero1 > 0:  # Mientras numero1 sea mayor que 0
            numero2 += 1  # numero2 se incrementa 
            numero1 -= 1  # numero1 se decrementa
        return numero2  # Regresa numero2
    else:  # Si no es verdad
        while numero1 < 0:  # Mientras numero1 sea menor que 0
            numero2 -= 1  # numero2 se decrementa 
            numero1 += 1  # numero1 se incrementa 
        return numero2  # Regresa numero2
    return suma(numero1, numero2)  # Regresa la función

resultado = suma(numero1, numero2)  # Pasamos el valor de la función a una variable

print(resultado)  # Imprimimos la variable
    