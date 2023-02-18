class Alumno:  # Creamos una clase

    __nombre = None  # Definimos una variable privada 
    __matricula = None  # Definimos una variable privada 
    __carrera = None  # Definimos una variable privada 


    def __init__(self):  # Constructor de la clase persona
        print("Alumnos\n")  # Imprime un mensaje
        
    def setNombre(self, nombre):  # Modifica el valor de la variable privada
        self.__nombre = nombre  # Asigna un nuevo valor a la variable privada

    def getNombre(self):  # Metodo para regresar el valor de la variable privada
        return self.__nombre  # Devuelve el valor de la variable privada

    def setMatricula(self, matricula):  # Modifica el valor de la variable privada
        self.__matricula = matricula  # Asigna un nuevo valor a la variable privada

    def getMatricula(self):  # Metodo para regresar el valor de la variable privada
        return self.__matricula  # Devuelve el valor de la variable privada

    def setCarrera(self, carrera):  # Modifica el valor de la variable privada
        self.__carrera = carrera  # Asigna un nuevo valor a la variable privada

    def getCarrera(self):  # Metodo para regresar el valor de la variable privada
        return self.__carrera  # Devuelve el valor de la variable privada


patricio = Alumno()  # Instanciamos un objeto llamado patricio

Yanet = Alumno()  # Instanciamos un objeto llamado yanet


patricio.setNombre("Patricio de Jesús")  # llama al metodo setNombre 
print(patricio.getNombre())  # LLama e imprime los datos del metodo getNombre
patricio.setMatricula("1722110158")  # llama al metodo setNombre 
print(patricio.getMatricula())  # LLama e imprime los datos del metodo getMatricula
patricio.setCarrera("Ingeniería en Desarrollo de Software Multiplataforma")
print(patricio.getCarrera())  # LLama e imprime los datos del metodo getCarrera

###################################

Yanet.setNombre("Yanet Molina Santos")  # Asignamos el valor al objeto yanet
print(Yanet.getNombre())  # LLama e imprime los datos del metodo getNombre
Yanet.setMatricula("1722110256")  # llama al metodo setNombre 
print(Yanet.getMatricula())  # LLama e imprime los datos del metodo getMatricula
Yanet.setCarrera("Ingeniería en Desarrollo de Software Multiplataforma")  # llama al metodo setNombre 
print(Yanet.getCarrera())  # LLama e imprime los datos del metodo getCarrera
