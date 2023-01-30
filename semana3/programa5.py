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

#  suma = numero1 + numero2  # No se puede concatener int con str

suma = int(numero1) + int(numero2)  # Suma las dos variables
print("La suma es: {}".format(suma))  # imprime la variable suma

resta = int(numero1) - int(numero2)  # Opera resta con casting
print("La resta es: {}".format(resta))  # imprime la variable resta  

multiplicacion = int(numero1) * int(numero2)  # Opera multiplicacion con casting
print("La multiplicacion es: {}".format(multiplicacion))  # imprime la variablemultiplicacion

division = int(numero1) / int(numero2)  # Opera divison con casting
print("La divison es: {}".format(division))  # imprime la variable divison

potencia = int(numero1) ** int(numero2)  # Opera potencia con casting
print("La potencia es: {}".format(potencia))  # imprime la variable potencia






