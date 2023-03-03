"""
    Reto25
    Nombre: Patricio de Jesús Vargas Ramírez
    Fecha: 02/03/2023
    Descripción: ¿Qué clase de IP es?
"""

ip = str(input("Ingresa tu ip: "))  # Pedimos que ingrese su ip

def tipo_clase(ip: str) -> str:  # Definimos una función teniendo la ip como clase

    octetos = ip.split(".")  # Separamos la ip por putnos

    primer_octeto = int(octetos[0])  # Guardamos el primer dato de la lista en una variable

    if primer_octeto >= 1 and primer_octeto <= 126:  # Si esa variable cumple estas dos condiciones
        print("La ip {} es Clase A" .format(ip))  # Imprimimos la ip con su clase correspondiente
    elif primer_octeto >= 128 and primer_octeto <= 191:  # Si esa variable cumple estas dos condiciones
        print("La ip {} es Clase B" .format(ip))  # Imprimimos la ip con su clase correspondiente
    elif primer_octeto >= 192 and primer_octeto <= 223:  # Si esa variable cumple estas dos condiciones
        print("La ip {} es Clase C" .format(ip))  # Imprimimos la ip con su clase correspondiente
    elif primer_octeto >= 224 and primer_octeto <= 239:  # Si esa variable cumple estas dos condiciones
        print("La ip {} es Clase D" .format(ip))  # Imprimimos la ip con su clase correspondiente
    else:  # Si ninguna fue verdadera
        print("La ip {} es Clase E" .format(ip))  # Imprimimos la ip con su clase correspondiente

tipo_clase(ip)  # Llamamos a la función
