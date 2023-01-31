"""
    Programa 6
    Nombre: Patricio de Jesús Vargas Ramírez
    Fecha: 30/01/2023
    Descripción: Calcular perimetro y área de un triangulo
"""
print("Calcular área y perimetro de un triangulo")
print("Ingrese lo que se pide")

lado1 = float(input("Medida de lado 1: "))
lado2 = float(input("Medida de lado 2: "))
lado3 = float(input("Medida de lado 3: "))

perimetro = lado1 + lado2 + lado3
s = perimetro / 2
area = (s * (s - lado1) * (s - lado2) * (s - lado3)) ** 0.5

arear = round(area, 2)

print("El perimetro del triangulo es = {}" .format(perimetro))
print("El area del triangulo es = {}" .format(arear))

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
