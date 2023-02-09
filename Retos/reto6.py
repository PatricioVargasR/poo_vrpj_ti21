"""
    Reto6
    Nombre: Patricio de Jesús Vargas Ramírez
    Fecha: 08/02/2023
    Descripción: Indice de masa corporal
"""

altura = float(input("Ingresa tu altura en metros: "))  # Ingresamos un valor
peso = float(input("Ingresa tu peso en kilogramos: "))  # Ingresamos un segundo valor

imc = peso / (altura ** 2)  # Calculamos el Indice de Masa Corporal

if imc < 18.5:  # Si IMC es menor a la medida
    print("Bajo peso")  # Imprime el siguiente mensaje
elif imc >= 18 and imc < 25:  # Hacemos doble comparación con and
    print("Peso normal")  # Imprimimos el siguiente mensaje
elif imc >=25 and imc < 30:  # Doble comparación con and
    print("Sobrepeso")  # Imprimimos el siguiente mensaje
else:  # Si ninguna fue
    print("Obesidad")  # Imprime este mensaje