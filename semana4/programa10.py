"""
    Programa 10
    Nombre: Patricio de Jesús Vargas Ramírez
    Fecha: 09/02/2023
    Descripción: 8 formas distintas con funcion
"""

def mayor(numero1, numero2):  # Definimos una función con dos parametros
    result = None  # Inicializamos una variable con None
    if numero1 > numero2:  # Comparamos para ver si numero1 es mayor
        result = numero1  # result obtiene el valor de numero1 en caso de ser verdadero
    elif numero2 > numero1:  # Comparamos para ver si numero2 es mayor
        result = numero2  # result obtiene el valor de numero1 en caso de ser verdadero
    return result  # Retornamos result

  # Invocamos la función
print(mayor(2,1))  # 2  
print(mayor(1,2))  # 2
print(mayor(2,2))  # None
print(mayor(2,-1))  # 2
print(mayor(-1,2))  # 2
print(mayor(-1,-1))  # None
print(mayor(-2,-1))  # -1
print(mayor(-1,-2))  # -1
