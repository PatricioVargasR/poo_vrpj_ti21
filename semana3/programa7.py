"""
    Programa 7
    Nombre: Patricio de Jesús Vargas Ramírez
    Fecha: 31/01/2023
    Descripción: Calcular e imprimir el área y perímetro de un circulo y un cuadrado
"""

print("Calcular área y perímetro de un círculo o cuadrado") # Imprime la función del programa
print("Seleccione una forma para calcular") # Imprime indicación

metodo = int(input("Ingrese 1 para elegir cuadrado o 2 para elegir circulo: ")) # Pide un valor en el teclado

if metodo == 1:  # Compara el valor ingresado en el teclado
  lado1 = float(input("Ingresa la medida de un lado: "))  # Se pide que ingrese el valor de un lado

  perimetro_cuadrado = lado1*4  # Opera el perimetro
  area_cuadrado = lado1*lado1  # Opera el area

  perimetro_cuadrado_redondeado = round(perimetro_cuadrado, 2)  # Se redondea el valor del perimetro
  area_cuadrado_redondeado = round(area_cuadrado, 2)  # Se redondea el valor del area
  
  print("El area de un cuadrado de {} cm por lado es: {} cm" .format(lado1, area_cuadrado_redondeado))  # Se imprime el valor redondeado del area
  print("El perimetro de un cuadrado de {} cm por lado es: {} cm" .format(lado1, perimetro_cuadrado_redondeado))  # Se imprime el valor redondeado del perimetro

elif metodo == 2:  # Compara el valor en caso de que haya sido falsa la expresión anterior
  
  radio = float(input("Ingresa la medida del radio: "))  # Pide el valor del radio 
  
  PI = 3.1416  # Creamos una constante
  
  area_circulo = (radio**2)*(PI)  # Operamos el area utilizando valores de teclado y una constante
  perimetro_circulo = (2*radio)*(PI)  # Operamos el area utilizando valores de teclado y una constante
  
  area_circulo_redondeado = round(area_circulo, 2)  # Redondeamos los decimales con round
  perimetror_circulo_redondeado = round(perimetro_circulo, 2)  # Redondeamos los decimales con round
  
  print("El área de un círculo de {} cm de radio es: {} cm" .format(radio, area_circulo_redondeado))  # Imprimimos el resultado de area redondeada 
  print("El perimetro de un círculo de {} cm de radio es: {} cm" .format(radio, perimetror_circulo_redondeado))  # Imprimimos el resultado de area redondeada 

else:  # Pasa a opción de "último" recurso
  print("La opción que elegiste no exite")  # Imprime un mensaje en caso de no haber coincidencia
  
  