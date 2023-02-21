"""
    Reto15
    Nombre: Patricio de Jesús Vargas Ramírez
    Fecha: 18/02/2023
    Descripción: ¿Cuántas palabras hay?
"""

cantidad = int(input("Ingrese la cantidad de términos que desea ver: "))  # Pedimos la cantidad de dígitos a mostrar

primer_numero, segundo_numero = 0, 1  # Inicializamos dos variables

# mostrar los términos de la serie de Fibonacci utilizando un ciclo while
while cantidad > 0:
    print(primer_numero)  # Imprimimos el valor guardador en la variable
    primer_numero, segundo_numero = segundo_numero, primer_numero +                                            segundo_numero  # Asignamos el valor de segundo_numero a primer_numero, además de sumar uno con otro guardandolo en el segundo_numero
    cantidad -= 1  # Disminuimos el valor de la cantidad

