"""
    Reto16
    Nombre: Patricio de Jesús Vargas Ramírez
    Fecha: 19/02/2023
    Descripción: ¿Esta frase es un palíndromo?
"""

cadena = str(input("Ingresa tu frase: "))  # Ingresamos una frase

def palindromo(cadena:str) -> str:  # Definimos una función tomando como parametro nuestra frase

    cadena_espacios = cadena.lower().replace(" ", "")  # Convertimos la frase en minusculas y eliminamos los espacios en blanco

    cadena_invertida = cadena_espacios[::-1]  # Invertimos la cadena

    if cadena_espacios == cadena_invertida:  # Comparamos si la palabra sin espacios es igual a la invertida 

        print("Tu frase: {} es un palíndromo" .format(cadena))  # Imprime la frase diciendo que si es un palíndromo
    
    else:  # Si no es verdadero

        print("Tu frase: {} no es un palíndromo" .format(cadena))  # Imprime la frase diciendo que no es un palíndromo


print(palindromo(cadena))  # Imprimimos el valor que obtuvo la función
