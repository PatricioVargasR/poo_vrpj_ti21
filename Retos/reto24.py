"""
    Reto24
    Nombre: Patricio de Jesús Vargas Ramírez
    Fecha: 28/02/2023
    Descripción: ¿Cuántas consonantes y consonantes?
"""

frase = str(input("Ingresa tu frase: "))  # Ingresa tu nueva frase

def cantidad(frase:str) -> str:  # Definimos una función tomando como parametro la frase

    frase = frase.lower()  # Convertimos a minusculas las frases
    
    num_vocales = 0  # Inicializamos el contador para las vocales
    num_consonantes = 0  # Inicializamos el contador para las consonantes
    
    for letra in frase:  # Iteramos por cada letra en la frase

        if letra in "aeiou":  # Si la letra es igual a una vocal
            num_vocales += 1  # El contador aumenta
        elif letra.isalpha():  # Si la letra es una consonante  # isalpha lo usamos para verificar que sean letras del alfabeto
            num_consonantes += 1  # El contador aumenta
            
    print("La cantidad de vocales es: {} y la cantidad de consonantes: {} " .format(num_vocales, num_consonantes))  # Imprimimos la cnatidad de vocales y consonantes

cantidad(frase)  # Llamamos a la función
        