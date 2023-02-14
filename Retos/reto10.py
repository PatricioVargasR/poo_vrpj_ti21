"""
    Reto10
    Nombre: Patricio de Jesús Vargas Ramírez
    Fecha: 12/02/2023
    Descripción:
"""

palabra = str(input("Ingrese su oración: "))  # Ingresamos un string desde el teclado

def cantidad_palabras(palabra:str) -> int:  # Definimos una función tomando el valor ingresado y devolviendo un entero
    
    palabras = len(palabra.split())  # Utilizamos split para dividir las cadenas ingresadas y len para contarlas
    return palabras  # Regresamos la variable

cantidad = cantidad_palabras(palabra)  # Guardamos el resultado de la función en una nueva variable

if cantidad == 1:  # Si el resultado es igual a 1
    print("La oración tiene {} palabra" . format(cantidad))  # Imprimos la cantidad 
elif cantidad == 0:  # Si el resultao es igual a 0
    print("No hay ninguna palabra")  # Imprimimos un mensaje
else:  # Si ninguna fue verdadera
    print("La oración tiene {} palabras" . format(cantidad))  # Imprimimos la cantidad 
