"""
    Patricio de Jesús Vargas Ramírez
    13/02/2023
    Descripción: Herencia
"""
# nombrepersona = str(input("Ingresa tu nombre: "))  # Pedimos un dato desde el teclado
# correopersona = str(input("Ingresa tu correo: "))  # Pedimos un dato desde el teclado

class Persona:  # Creamos una clase

#    nombre = None  # Inicializamos una variable
    __nombre = None  # Varriable privada
    __email = None  # Variable privada

    def __init__(self):  # Metodo para ejecutar la clase
#        __email = None  # Otra forma de iniciar variables globales
        print("Persona: ")  # Se imprime Persona
        
    def setNombre(self, nombre):  # Modificar los valores
        self.__nombre = nombre  # Guardamos el valor en la variable privada

    def getNombre(self):  # Llama al valor
        return self.__nombre  # Regresamos el valor

    #########################################

    def setEmail(self, email):  # Modificamos el valor de la variable privada
        self.__email = email  # Asignamos un valor a la variable
    
    def getEmail(self):  # Llama al valor
        return self.__email  # Regresamos el valor


 # Instancia de una clase
dejah = Persona()  # Hacemos una copia
patricio = Persona()  # Hacemos otra copia

 # LLamamos a una variable privada
dejah.setNombre("Dejah")  # Damos un valor
print(dejah.getNombre())  # Llamamos ese valor

 # LLamamos a una variable privada
dejah.setEmail("Dejah@google.com")  # Damos un valor
print(dejah.getEmail())  # Llamamos ese valor

# Nueva Persona
patricio.setNombre("Patricio")  # Damos un valor
print(patricio.getNombre())  # Llamamos ese valor

patricio.setEmail("varrapa25@gmail.com")  # Damos un valor
print(patricio.getEmail())  # Llamamos ese valor

#########################################
# print(dejah.__nombre)  # Accedemos a un atributo
# jhon = Persona()  # Instancia de una clase
