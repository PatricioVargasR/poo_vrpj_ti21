"""
    Programa 4
    Nombre: Patricio de Jesús Vasgas Ramírez
    Fecha: 26/01/2023
    Descripción: Acceso a las variables por posición y por nombres
"""

numero1 = 10  # Variable de tipo int
numero2 = 5  # Variable de tipo int

# Acceder a las variables por posición

print("{} + {} = {}".format(numero1, numero2, numero1 + numero2))  # 10 + 5 = 15

# print("{} + {} = ".format(numero1, numero2, numero1 + numero2))  # 10 + 5 = 

# print("{} + {} = {}".format(numero1, numero2))   # No existe el indice 3
      
print("{n1} + {n2} = {suma}".format(n1=numero1, n2=numero2, suma=numero1 + numero2))  # Asignar variables
      
# print("{n2} + {n2} = {suma}" .format(n1=numero1, n2=numero2, suma=numero1+numero2))  # Identificación de variables

# print("{n4} + {n4} = {n4}" .format(n1=numero1, n2=numero2, suma=numero1+numero2))  # Identificación de variables

print("{numero1} + {numero2} = {suma}" .format(numero1=numero1, numero2=numero2, suma=numero1+numero2))  # Por mismo nombre

# print("{numero1} + {numero2} = ".format(numero1, numero2, numero1 + numero2))  # 10 + 5 = 15

# KeyError es por que no encuentra el nombre de la variable      