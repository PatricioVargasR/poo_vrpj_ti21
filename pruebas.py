print("Calcular área y perímetro de un círculo o cuadrado") # Imprime la función del program
print("Seleccione una forma para calcular") # Imprime indicación

while True:
    metodo = input("Ingrese 1 para elegir cuadrado o 2 para elegir circulo: ") # Pide un valor en el teclado
    try:
      metodo = int(metodo)
    except ValueError:
      print("El valor ingresado no es un número. Intente de nuevo.")
      continue
    if metodo == 1:  # Compara el valor ingresado en el teclado
      while True:
        lado1 = input("Ingresa la medida de un lado: ")  # Se pide que ingrese el valor de un lado
        try:
          lado1 = float(lado1)
          break
        except ValueError:
          print("El valor ingresado no es un número. Intente de nuevo.")
          continue
      print(lado1)
      break
    elif metodo == 2:  # Compara el valor en caso de que haya sido falsa la expresión anterior
      while True:
        radio = input("Ingresa la medida del radio: ")  # Pide el valor del radio 
        try:
          radio = float(radio)
          break
        except ValueError:
          print("El valor ingresado no es un número. Intente de nuevo.")
          continue
      print(radio)
      break
    else:  # Pasa a opción de "último" recurso
      print("El valor ingresado no es válido. Intente de nuevo.")
      continue
