"""
    Reto11
    Nombre: Patricio de Jesús Vargas Ramírez
    Fecha: 13/02/2023
    Descripción: Uso de clases
"""

class Perro:  # Creamos una clase

    __nombre = None  # Variable privada
    __raza = None  # Variable privada
    __peso = None  # Variable privada
    __edad = None  # Variable privada
    
    def __init__(self):  # Método init para inicar la clase
        print("Perro: ")  # Imprime Perro

    def setNombre(self, nombre):  # Llamamos al valor
        self.__nombre = nombre  # Lo guardamos

    def getNombre(self):  # Traemos el valor
        return self.__nombre  # Lo devolvemos

    def setRaza(self, raza):  # Llamamos al valor
        self.__raza = raza  # Lo guardamos

    def getRaza(self):  # Traemos el valor
        return self.__raza  # Lo devolvemos

    def setPeso(self, peso):  # Llamamos al valor
        self.__peso = peso  # Lo guardamos

    def getPeso(self):  # Traemos el valor
        return self.__peso  # Lo devolvemos

    def setEdad(self, edad):  # Llamamos al valor
        self.__edad = edad  # Lo guardamos

    def getEdad(self):  # Traemos el valor
        return self.__edad  # Lo devolvemos


chencha = Perro()  # Instanciamos una clase

chencha.setNombre("Chencha")  # Le damos un valor
print(chencha.getNombre())  # Imprimimos ese valor
chencha.setRaza("Cruza")  # Le damos un valor
print(chencha.getRaza())  # Imprimimos ese valor
chencha.setPeso("25 kg")  # Le damos un valor
print(chencha.getPeso())  # Imprimimos ese valor
chencha.setEdad("10 años")  # Le damos un valor
print(chencha.getEdad())  # Imprimimos ese valor