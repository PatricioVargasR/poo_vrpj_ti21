"""
    Programa 5
    Nombre: Patricio de Jesús Vargas Ramírez
    Fecha: 30/01/2023
    Descripción: Transformar valores 
    a otro tipo de dato(Casting) 
    y realizar operaciones
"""
numero1 = input("Numero1: ")  # Pide un valor en el teclado
numero2 = input("Numero2: ")  # Asignamos valor

suma = int(numero1) + int(numero2)  # Suma las dos variables
#  suma = numero1 + numero2  # No se puede concatener int con str

resta = int(numero1) - int(numero2)
multiplicacion = int(numero1) * int(numero2)
division = int(numero1) / int(numero2)
potencia = int(numero1) ** int(numero2)

print("La suma es: {}".format(suma))  # imprime la variable suma
print("La resta es: {}".format(resta))
print("La multiplicacion es: {}".format(multiplicacion))
print("La divison es: {}".format(division))
print("La potencia es: {}".format(potencia))
