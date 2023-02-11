"""
    Programa 9
    Nombre: Patricio de Jesús Vargas Ramírez
    Fecha: 07/02/2023
    Descripción: 11 formas diferentes de comparar dos  
    numeros escribiendo el mayor o none en caso de ser
    igual
"""

n1 = int(input("Número 1: "))  # Pide un valor desde el teclado
n2 = int(input("Número 2: "))  # Pide un valor desde el teclado

# Forma 1
if n1 > n2:  # Se verifica que n1 sea mayor
    print(n1)  # Imprime n1
if n2 > n1:  # Se verifica que n2 sea mayor
    print(n2)  # Imprime n2
if n1 == n2:  # Se verifica que ambos sean iguales
    print(None)  # Imprime un None
    
# Forma 2
if n2 > n1:  # Se verifica que n2 sea mayor
    print(n2)  # Imprime n2
if n1 > n2:  # Se verifica que n1 sea mayor
    print(n1)  # Imprime n1
else:  # Si ninguna es verdadera
    print(None)  # Imprime un None
    
# Forma 3
if n1 > n2:  # Se verifica que n1 sea mayor
    print(n1)  # Imprime n1
elif n2 > n1:  # Se verifica que n2 sea mayor
    print(n2)  # Imprime n2
else:  # Si ninguna es verdadera
    print(None)  # Imprime un None

# Forma 4
if n1 == n2:  # Se verifica que ambas sean iguales
    print(None)  # Imprime un None
if n1 > n2:  # Se verifica que n1 sea mayor
    print(n1)  # Imprime n1
if n2 > n1:  # Se verifica que n2 sea mayor
    print(n2)  # Imprime n2

# Forma 5
if n1 < n2:  # Se verifica que n1 sea menor
    print(n2)  # Imprime n2
if n2 < n1:  # Se verifica que n2 sea menor
    print(n1)  # Imprime n1
if n1 == n2:  # Se verifica que sean iguales
    print(None)  # Imprime un None

# Forma 6
if n2 > n1:  # Se verifica que n2 sea mayor
    print(n2)  # Imprime n2
if n2 < n1:  # Se verifica que n2 sea menor
    print(n1)  # Imprime n1
else:   # Si ninguna fue verdadera
    print(None)  # Imprime un None

# Forma 7
if(n2<n1>n2):  # Se verifica que n2 sea menor en dos ocasiones
    print(n1)  # Imprime n1
elif(n1<n2>n1):  # Se verifica que n1 sea menor en dos ocasiones
    print(n2)  # Imprime n2
else:  # Si ninguna fue verdadera
    print(None)  # Imprime un None

# Forma 8
if n1 <= n2:  # Se verifica que n1 sea menor o igual 
    if n1 == n2:  # Se verifica que ambos números son iguales
        print(None)  # Imprime un None
    else:  # Si no es verdadera
        print(n2)  # Imprime n2
else:  # Si no es verdadera
    print(n1)  # Imprime n1

# Forma 9 (Propia)
if n1 != n2:  # Se verifica que ambos sean diferentes
    if n1>n2:  # Se verifica que n1 sea mayor
        print(n1)  # Imprime n1
    else:  # Si no es verdadera
        print(n2)  # Imprime n2
else:  # Si no es verdadera
    print(None)  # Imprime un None

# Forma 10(Propia)
if n1 != n2 and n1 > n2:  # Se verifica que ambos números sean diferentes y que n1 sea mayor 
    print(n1)  # Imprime n1
elif n2 > n1:  # Se verifica que n2 sea mayor
    print(n2)  # Imprime n2
else:  # Si ninguna es verdadera
    print(None)  # Imprime un None

# Forma 11(Propia)
if n1 != n2 and n2 > n1:  # Se verifica que ambos números sean diferentes y que n2 sea mayor
    print(n2)  # Imprime n2
elif n1 > n2:  # Se verifica que n2 sea mayor
    print(n1)  # Imprime n1
else:   # Si ninguna es verdadera
    print(None)  # Imprime un None
