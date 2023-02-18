"""
    Nombre: Patricio de Jesús Vargas Ramírez
    Fecha: 16/02/2023
    Descripción: Trabajar con clases en diferentes archivos

"""

class Persona:  # Creamos una clase

    __nombre = None  # Definimos una variable privada 
    
    def __init__(self) -> None:  # Constructor de la clase persona
            print("Constructor Persona")  # Imprime un mensaje

    def setNombre(self, nombre:str) -> None:  # Modifica el valor de la variable privada
        self.__nombre = nombre  # Asigna un nuevo valor a la variable privada
    
    def getNombre(self) -> str:  # Metodo para regresar el valor de la variable privada
        return self.__nombre  # Devuelve el valor de la variable privada
