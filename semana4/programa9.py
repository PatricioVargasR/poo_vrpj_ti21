"""
    Programa 9
    Nombre: Patricio de Jesús Vargas Ramírez
    Fecha: 07/02/2023
    Descripción: 11 formas diferentes de comparar dos  
    numeros escribiendo el mayor o none en caso de ser
    igual
"""


n1 = int(input("Número 1: "))
n2 = int(input("Número 2: "))


# Forma 1
if n1 > n2:
    print(n1)
if n2 > n1:
    print(n2)
if n1 == n2:
    print(None)
        
# Forma 2
if n2 > n1:
    print(n2)
if n1 > n2:
    print(n1)
else:
    print(None)
    
# Forma 3
if n1 > n2:
    print(n1)
elif n2 > n1:
    print(n2)
else:
    print(None)

# Forma 4
if n1 == n2:
    print(None)
if n1 > n2:
    print(n1)
if n2 > n1:
    print(n2)

# Forma 5
if n1 < n2:
    print(n2)
if n2 < n1:
    print(n1)
if n1 == n2:
    print(None)

# Forma 6
if n2 > n1:
    print(n2)
if n2 < n1:
    print(n1)
else: 
    print(None)

# Forma 7
if(n2<n1>n2):
    print(n1)
elif(n1<n2>n1):
    print(n2)
else:
    print(None)

# Forma 8
if n1 <= n2:
    if n1 == n2:
        print(None)
    else:
        print(n2)
else:
    print(n1)

# Forma 9 (Propia)
if n1 != n2:
    if n1>n2:
        print(n1)
    else:
        print(n2)
else:
    print(None)

# Forma 10(Propia)
if n1 != n2 and n1 > n2:
    print(n1)
elif n2 > n1:
    print(n2)
else:
    print(None)

# Forma 11(Propia)
if n1 != n2 and n2 > n1:
    print(n2)
elif n1 > n2:
    print(n1)
else: 
    print(None)
