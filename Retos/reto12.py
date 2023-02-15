"""
    Reto12
    Nombre: Patricio de Jesús Vargas Ramírez
    Fecha: 13/02/2023
    Descripción: Uso de la herencia
"""

class Persona:

    __nombre = None
    __edad = None
    __telefono = None

    def __init__(self):
        print("Persona")

    def setNombre(self, nombre):
        self.__nombre = nombre

    def getNombre(self):
        return self.__nombre

class Alumno(Persona):

    __matricula = None
    __nombre = None
    __carrera = None

    def __init__(self):
        super().__init__()
        print("Alumno")

    def setMatricula(self, matricula):
        self.__matricula = matricula

    def getMatricula(self):
        return self.__matricula

    def setNombre(self, nombre):
        self.__nombre = nombre

    def getNombre(self):
        return self.__nombre

    def setCarrera(self, carrera):
        self.__carrera = carrera

    def getCarrera(self):
        return self.__carrera

class Coordinador(Persona):

    __no_nomina = None
    __carrera_a_cargo = None

    def __init__(self):
        super().__init__()
        print("Coordinador")

    def setNoNomina(self, no_nomina):
        self.__no_nomina = no_nomina

    def getNoNomina(self):
        return self.__no_nomina

    def setCarreraCargo(self, carrera_a_cargo):
        self.__carrera_a_cargo = carrera_a_cargo

    def getCarreraCargo(self):
        return self.__carrera_a_cargo

class Profesor(Persona):

    __no_nomina = None
    __horarios = None
    __materias = None

    def __init__(self):
        super().__init__()
        print("Profesor")

    def setNoNomina(self, no_nomina):
        self.__no_nomina = no_nomina

    def getNoNomina(self):
        return self.__no_nomina

    def setHorarios(self, horarios):
        self.__horarios = horarios

    def getHorarios(self):
        return self.__horarios

    def setMaterias(self, materias):
        self.__materias = materias

    def getMaterias(self):
        return self.__materias

objeto_persona = Persona()
objeto_alumno = Alumno()
objeto_coordinador = Coordinador()
objeto_profesor = Profesor()
