"""
    Reto23
    Nombre: Patricio de Jesús Vargas Ramírez
    Fecha: 28/02/2023
    Descripción: Uso de librerías para conocer la fecha actual
"""
import datetime

decision = int(input("Elija 1 si quiere ver el día, 2 si quiere ver el mes, 3 si quiere ver el año y 4 la fecha completa: "))  # Damos diferentes elecciones

def fecha(decision:int) -> int:  # Definimos una función tomando el número seleccionado como parametro
    
    fecha_actual = datetime.date.today()  # Definiamos la fecha actual
    dia = fecha_actual.day  # Creamos un día
    mes = fecha_actual.month  # Un mes
    año = fecha_actual.year  # Un año
    
    if decision == 1:  # Si la decision fue 1
        print("El día es: {}" .format(dia))  # Imprimimos día
    elif decision == 2:  # Si la decision fue 2
        print("El mes es: {}" .format(mes))  # Imprimimos mes
    elif decision == 3:  # Si la deision fue 3
        print("El año es: {}" .format(año))  # Imprimimos año
    elif decision == 4:  # Si la decision fue 4
        print("La fecha actual es: {}/{}/{}" .format(dia, mes, año))  # Imprimimos fecha completa
    else:  # Si no fue ninguna de las anteriores
        print("No ingreso una opción valida")  # Imprimimos mensaje

fecha(decision)  # Llamamos a la función
