"""
    Patricio de Jesús Vargas Ramírez
    14/02/2023
    Descripción: Herencia
"""

class Persona:  # Creamos una clase llamada Persona

    __nombre = None  # Incializamos una variabla privada 
    __edad = None  # Inicializamos una variable privada

    def __init__(self):  # Constructor de la clase Persona
        print("Persona")  # Imprime el mensaje Persona

    def setNombre(self, nombre):  # Modificador de la varible nombre
        self.__nombre = nombre  # Asignamos un nuevo valor a la varible

    def getNombre(self):  # Llamamos al valor de la variable
        return self.__nombre  # Regresamos el valor de la variable

    def setEdad(self, edad):  # Modificador de la varible edad
        self.__edad = edad  # Asignamos un nuevo valor a la varible
    
    def getEdad(self):  # Llamamos al valor de la variable
        return self.edad  # Regresamos el valor de la variable

class Alumno(Persona):  # Creamos una clase llamda Alumno que hereda de Persona 

    __matricula = None  # Creamos una variable privada

    def __init__(self):  # Constructor de la clase Alumno
        super().__init__()  # Llamamos al constructor de la super clase
        print("Alumno")  # Imprime Alumno

    def setMatricula(self, matricula):  # Modificador de la varible matricula
        self._matricula = matricula  # Asignamos un nuevo valor a la varible
    
    def getMatricula(self):  # Llamamos al valor de la variable
        return self.__matricula  # Regresamos el valor de la variable
    

objeto_persona = Persona()  # Instanciamos una clase
objeto_alumno = Alumno()  # Instanciamos una clase 

print(dir(objeto_persona))  # Imprimimos el directorio del objeto persona
print(dir(objeto_alumno))  # Imprimimos el directorio del objeto persona
