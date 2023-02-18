"""
    Patricio de Jesús Vargas Ramírez
    14/02/2023
    Descripción: Herencia con varias subclases
"""

class Persona:  # Creamos una clase

    __nombre = None  # Inicializamos una variable privada
    __edad = None  # Inicializamos una variable privada

    def __init__(self):  # Metodo para almacenar todo lo de la clase
        print("Persona")  # Imprime persona

    def setNombre(self, nombre):  # Obtiene un valor para nombre
        self.__nombre = nombre  # Almacena el valor

    def getNombre(self):  # Llama al valor 
        return self.__nombre  # Regresa el valor de la variable

    def setEdad(self, edad):  # Modifica el valor de la variable
        self.edad = edad  # Asigna el valor de la variable
    
    def getEdad(self):  # Metodo para regresar el valor ingresado
        return self.edad  # Regresamos el valor de la variable

class Alumno(Persona):  # Creamos una clase heredando atributos de persona

    __matricula = None  # Inicializamos una variable privada
    __nombre = None  # Inicializamos una variable privada

    def __init__(self):  # Almacena todo lo de la clase
        super().__init__()  # Llamamos a todo elemento de la super clase
        print("Alumno")  # Imprime Alumno

    def setMatricula(self, matricula):  # Obtenemos un valor para matricula
        self._matricula = matricula  # Guardamos el valor 

    def getMatricula(self):  # Llamamos al valor
        return self.__matricula  # Regresamos el valor

    def setNombre(self, nombre):  # Obtenemos un valor para nombre
        self.nombre = nombre  # Guardamos el valor

    def getNombre(self):  # Llamamos el valor
        return self.__nombre  # Regresamos el valor    

class Coordinador(Persona):  # Creamos una clase heredando atributos de persona

    __no_nomina = None  # Creamos una varible privada
    __carrera_a_cargo = None  # Creamos una variable privada  
    
    def __init__(self):  # Constructor de la clase Coordinador
        super().__init__()  # Llamamos al constructor de la clase Persona
        print("Coordinador")  # Imprime Coordinador

    def setNoNomina(self, no_nomina):  # Modifica el valor de la variable privada
        self.__no_nomina = no_nomina  # Asigna un nuevo valor a la variable privada

    def getNoNomina(self):  # Metodo para regresar el valor de la variable privada
        return self.__no_nomina  # Devuelve el valor de la variable privada

    def setCarreraCargo(self, carrera_a_cargo):  # Modifica el valor de la variable privada
        self.__carrera_a_cargo = carrera_a_cargo  # Asigna un nuevo valor a la variable privada

    def getCarreraCargo(self):  # Metodo para regresar el valor de la variable privada
       return self.__carrera_a_cargo   # Devuelve el valor de la variable privada

class Profesor(Persona):  # Creamos una clase heredando atributos de persona

    __no_nomina = None  # Inicializamos una variable privada

    def __init__(self):  # Constructor de la clase Profesor
        super().__init__()  # Llamamos al constructor de la clase Persona
        print("Profesor")  # Imprime Profesor

    def setNoNomina(self, no_nomina):  # Modifica el valor de la variable privada
         self.__no_nomina = no_nomina  # Asigna un nuevo valor a la variable privada
    
    def getNoNomina(self):  # Metodo para regresar el valor de la variable privada
        return self.__no_nomina  # Devuelve el valor de la variable privada


objeto_persona = Persona()  # Instanciamos un objeto llamado objeto_persona
objeto_alumno = Alumno()  # Instanciamos un objeto llamado objeto_alumno
objeto_profesor = Profesor()  # Instanciamos un objeto llamado objeto_profesor
objeto_coordinador = Coordinador()  # Instanciamos un objeto llamado objeto_coordinador

#  print(dir(objeto_persona))  # Imprime el directorio del objeto persona
#  print(dir(objeto_alumno))  # Imprime el directorio del objeto alumno
