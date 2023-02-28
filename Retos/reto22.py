"""
    Reto22
    Nombre: Patricio de Jesús Vargas Ramírez
    Fecha: 27/02/2023
    Descripción: ¿Mayusculas o Minusculas?
"""

decision = str(input("Presiona Y para Mayusculas o X para Minusculas: "))

def reescribir(decision: str)-> str:

    decision = decision.lower()
    
    if decision == "y":
        palabra = str(input("Ingresa tu palabra o frase: "))

        palabra = palabra.upper()
        print("Tu palabra o frase reescrita es: {}" .format(palabra))

    elif decision == "x":
        palabra = str(input("Ingresa tu palabra o frase"))

        palabra = palabra.lower()
        print("Tu palabra o frase reescrita es: {} " .format(palabra))

    else:
        print("No has escrito ninguna de las opciones disponibles")

reescribir(decision)