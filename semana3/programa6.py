"""
    Programa 6
    Nombre: Patricio de Jesús Vargas Ramírez
    Fecha: 30/01/2023
    Descripción: Calcular perimetro y área de un triangulo
"""
print("Calcular área y perimetro de un triangulo")  # Imprime la función del programa
print("Ingrese lo que se pide")  # Imprime indicación

lado1 = float(input("Medida de lado 1: "))  # Pide un valor en el teclado
lado2 = float(input("Medida de lado 2: "))  # Pide un valor en el teclado
lado3 = float(input("Medida de lado 3: "))  # Pide un valor en el teclado

perimetro = lado1 + lado2 + lado3  # Opera los tres valores ingresados sumandolos entre si
s = perimetro / 2  # Almacena en una nueva variable el resultado de operar el anterior resultado
area = (s * (s - lado1) * (s - lado2) * (s - lado3)) ** 0.5  # Calculamos el area con formula de Herón

arear = round(area, 2)  # Redondeamos el area a 2 decimales con round

print("El perimetro del triangulo es = {}" .format(perimetro))  # Imprimimos el perimetro con format
print("El area del triangulo es = {}" .format(arear))  # Imprimimos el area con format

  # Opción dos

"""
base = float(input("Medida de la base: "))
altura = float(input("Medida de la altura: "))
lado1 = float(input("Mediada de Lado 1: "))
lado2 = float(input("Mediada de Lado 2: "))

area = (base*altura) / 2
arear = round(area, 2)
perimetro = lado1 + lado2 + base

print("El area del triangulo es = {}" .format(arear))
print("El perimtro del triangulo es = {}" .format(perimetro))

"""
