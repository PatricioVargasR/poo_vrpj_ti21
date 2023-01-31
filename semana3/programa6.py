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
base = float(input("Medida de la base: "))  # Pedimos la base desde el teclado
altura = float(input("Medida de la altura: "))  # Pedimos la altura desde el teclado
lado1 = float(input("Mediada de Lado 1: "))  # Pedimos la medida de un lado desde el teclado
lado2 = float(input("Mediada de Lado 2: "))  # Pedimos la medida del ultimo lado desde el teclado

area = (base*altura) / 2  # Operamos la area
arear = round(area, 2)  # Redondeamos los puntos decimales
perimetro = lado1 + lado2 + base  # Calculamos el perimetro

print("El area del triangulo es = {}" .format(arear))  # Imprimimos el area con format
print("El perimtro del triangulo es = {}" .format(perimetro))  # Imprimimos el perimetro con format
"""
  # Opción tres

"""
print("Calcular área y perímetro de un triángulo") # Imprime la función del programa
print("Seleccione un método para calcular") # Imprime indicación

metodo = int(input("Ingrese 1 para calcular con medida de los lados o 2 para calcular con medida de base y altura: ")) # Pide un valor en el teclado

if metodo == 1:  # Compara el valor que se introdujo en el teclado 
  lado1 = float(input("Medida de lado 1: ")) # Pide un valor en el teclado
  lado2 = float(input("Medida de lado 2: ")) # Pide un valor en el teclado
  lado3 = float(input("Medida de lado 3: ")) # Pide un valor en el teclado
  
  perimetro = lado1 + lado2 + lado3  # Opera los tres valores ingresados sumandolos entre sí
  s = perimetro / 2  # Almacena en una nueva variable el resultado de operar el anterior resultado
  area = (s * (s - lado1) * (s - lado2) * (s - lado3)) ** 0.5  # Calculamos el área con fórmula de Herón
  
  arear = round(area, 2)  # Redondeamos el área a 2 decimales con round
  
  print("El perímetro del triángulo es = {}" .format(perimetro))  # Imprimimos el perímetro con format
  print("El área del triángulo es = {}" .format(arear))  # Imprimimos el área con format

else:  # En caso de que la decisión sea falsa, calcula la area/perimetro de otra manera
  base = float(input("Medida de la base: "))  # Ingresa la base desde el teclado
  altura = float(input("Medida de la altura: "))  # Ingresa la alturadesde el teclado
  lado1 = float(input("Mediada de Lado 1: "))  # Ingresa un lado desde el teclado
  lado2 = float(input("Mediada de Lado 2: "))  # Ingresa otro lado desde el teclado
  
  area = (base*altura) / 2  # Opera la area
  arear = round(area, 2)  # Redondea los decimales
  perimetro = lado1 + lado2 + base  # Opera el perimetro
  
  print("El área del triángulo es = {}" .format(arear))  # Imprime el area redondeada
  print("El perímetro del triángulo es = {}" .format(perimetro))  # Imprime el perimetro
"""
