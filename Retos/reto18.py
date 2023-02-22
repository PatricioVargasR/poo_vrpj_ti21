"""
    Reto18
    Nombre: Patricio de Jesús Vargas Ramírez
    Fecha: 22/02/2023
    Descripción: Tablas de multiplicar con while
"""

numero = int(input("Ingrese que tabla de multiplicar quiere ver: "))  # Pedimos que ingrese el número de la tabla de multiplicar

def tabla_multiplicar(numero:int) -> int:  # Definimos una función la cual tomará de parametro el numero ingresado y devolverá un entero

    contador = 1  # Inicializamos un contador
    
    while contador <= 10:  # Minetras el contador sea menor o igual a 10, ejecutará el siguiente bloque
        
        multiplicar = numero * contador  # Hacemos la operación para sacar la multiplicación correspondiente
        print("{} X {} = {}" .format(numero, contador, multiplicar))  # Imprimos la mutiplicacion llamando al numero, contador y a la variable multiplicar
        contador += 1  # Aumentamos el contador en 1
        
tabla_multiplicar(numero)  # Llamamos a la función