from persona import Persona  # Importamos del archivo persona.py la clase Persona

"""
    Nombre: Patricio de Jesús Vargas Ramírez
    Fecha: 16/02/2023
    Descripción: Trabajar con clases en diferentes archivos

"""

class Alumno(Persona):  # Creamos una clase heredando atributos de Persona

    def __init__(self) -> None:  # Constructor de la clase Alumno
        super().__init__()  # Llamo al consructuro de la clase Persona
        print("Constructor Alumno")  # Muestra un mensaje


objeto_alumno = Alumno()  # Creamos un objeto de la clase Alumno e invoca al constructor
objeto_alumno.setNombre("Dejah")  # llama al metodo setNombre de la clase Persona
print(objeto_alumno.getNombre())  # LLama e imprime los datos del metodo getNombre