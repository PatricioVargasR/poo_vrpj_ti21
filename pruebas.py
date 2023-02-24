
numero = int(input("Ingresa el numero de tablas que quiers ver: "))
numero += 1

for i in range(1,numero):
    print("Tabla del {}" .format(i))

    for j in range(1,11):
        multplicar = i * j 
        print("{} * {} = {}" .format(i, j, multplicar))
