"""
    Reto20
    Nombre: Patricio de Jesús Vargas Ramírez
    Fecha: 23/02/2023
    Descripción: Palabras son anagramas
"""

palabra1 = str(input("Ingrese su primera palabra: "))  # Pedimos un palabra
palabra2 = str(input("Ingrese su segunda palabra: "))  # Pedimos una segunda palabra

def tabla_multiplicar(palabra1:str, palabra2:str) -> str:  # Definimos una función con dos parametros y devolverá un str

    if len(palabra1) != len(palabra2):  # Se compara el tamaño de las dos palabras
        print("Las palabras no son anagramas")  # En acaso de que sea verdad, imprime un mensaje
    
    else:  # Si no es verdad

        palabra1 = palabra1.lower()  # Convertimos todo en minusculas en la palabra1
        palabra2 = palabra2.lower()  # Convertimos todo en minusculas en la palabra2

        lista1 = sorted(list(palabra1))  # Convertimos las palabra1 en lista y la ordenamos
        lista2 = sorted(list(palabra2))  # Convertimos la palabra2 en lista y la ordenamos

        if lista1 == lista2:  # Se compara que las listas sean iguales
            print("Las palabras son anagramas")  # Se imprime el mensaje en caso de que sea verdad
        else:  # Si es falso
            print("Las palabras no son anagramas")  # Se imprime este mensaje

tabla_multiplicar(palabra1, palabra2)  # Se llama a la función
