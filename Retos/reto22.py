"""
    Reto22
    Nombre: Patricio de Jesús Vargas Ramírez
    Fecha: 27/02/2023
    Descripción: ¿Mayusculas o Minusculas?
"""

decision = str(input("Presiona Y para Mayusculas o X para Minusculas: "))  # Ingresamos una cadena de texto

def reescribir(decision: str)-> str:  # Creaomos una funció con la cadena como parametro

    decision = decision.lower()  # Hacemos todo minusculas
    
    if decision == "y":  # Si la decisión es y
        palabra = str(input("Ingresa tu palabra o frase: "))  # Pedimos que ingrese una cadena

        palabra = palabra.upper()  # Convertimos todo a Mayuscula
        print("Tu palabra o frase reescrita es: {}" .format(palabra))  # La imprimimos

    elif decision == "x":  # Si la decisión fue x
        palabra = str(input("Ingresa tu palabra o frase"))  # Pedimos una cadena
 
        palabra = palabra.lower()  # Convertimos todo a Minusculas
        print("Tu palabra o frase reescrita es: {} " .format(palabra))  # Imprimimos la cadena

    else:  # Si no fue ninguna
        print("No has escrito ninguna de las opciones disponibles")  # Imprime un mensaje

reescribir(decision)  # Llamamos a la función
