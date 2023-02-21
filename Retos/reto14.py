"""
    Reto14
    Nombre: Patricio de Jesús Vargas Ramírez
    Fecha: 17/02/2023
    Descripción: ¿Cuántas palabras hay?
"""

oracion = str(input("Ingresa una oración: "))  # Ingresamos la oración

def cantidad(oracion):  # Definimos una función teniendo como parametros las variables anteriores
    
    numero_palabras = len(oracion.split())  # Usamos split dividir la oración en palabras y len para contarlas
    
    if numero_palabras == 0:  # Sí el número de palabras es cero
        cantidad = numero_palabras  # cantidad adquiere el valor de numero_palabras
    elif numero_palabras == 1:  # Sí el número de palabras es uno
        cantidad = numero_palabras  # cantidad adquiere el valor de numero_palabras
    else:  # Si ninguna de las anteriores se cumple
        cantidad = numero_palabras  # cantidad adquiere el valor de numero_palabras
    return cantidad  # Regresa el valor

numero_palabra = cantidad(oracion)  # El valor de la función se le pasa a una variable 

print("La oración tiene {} palabras" .format(numero_palabra))  # Imprime esa variable
