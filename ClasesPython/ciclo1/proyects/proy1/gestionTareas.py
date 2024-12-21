from datetime import datetime
import statistics

class Tarea:
    
    #funcion de inicializacion = metodo conatructor
    def __init__(self, nombre,fechaLimite, categoria, horasDedicadas):
        self.nombre = nombre
        self.fechaLimite = fechaLimite
        self.categoria = categoria
        
#funcion para agregar una tarea
def agregarTarea(listaTareas):
    nombre = input('Ingrese el nombre de la tarea: ')
    fechaLimite_str = input('ingrese la fecha limite de la tarea (DD/MM/YYYY): ')
    try:
        fechaLimite = datetime(fechaLimite_str, "%d/%m/%Y")
    except ValueError:
        print('fecha no valida, por favor ingrese la fecha como aparece hay (DD/MM/YYYY)')
        return
    categoria = input("ingreselas categorias de las tareas (Estudio, Personal, Trabajo, etc): ")
    horasDedicadas_str = input("ingrese las horas dedicadas a la tarea, separadas en comas: ")
    try:
        horasDedicadas = list(map(float, horasDedicadas_str.split(",")))
    except ValueError:
        print('las horas deben ser numericas')
        return
    
    #crar un objeto y lo agrega a la lista de tareas
    tarea = Tarea(nombre, fechaLimite, categoria, horasDedicadas)
    listaTareas.append(tarea)
    print('tarea agregada exictosamente....')
    
#crear funcion para vizualizar las tareas
def visualizarTareas(listaTareas):
    if not listaTareas:
        print('no hay tareas para vizualizar')
        return
    
    for i, tarea in enumerate(listaTareas, start=1):
        print(f'\n Tarea{i}')
        print(f'Nombre: {tarea.nombre}')
        print(f'Fecha Limite: {tarea.fechaLimite.strftime("%d/%m/%Y")}')
        print(f'Categorias: {tarea.categorias}')
        print(f'Horas dedicadas: {tarea.horasDedicadas}')
        
# funcion para analizar tareas
def analizarTareas(listaTareas):
    if not listaTareas:
        print('no hay tareas para analizar')
        return
    
    for tarea in listaTareas:
        promedio = statistics.mean(tarea.horasDedicadas)
        maximo = max(tarea.horasDedicadas)
        minimo = min(tarea.horasDedicadas)
        print(f'\nTarea: {tarea.nombre}')
        print(f'Promedio de horas dedicadas: {promedio}')
        print(f'maximo de horas dedicadas: {maximo}')
        print(f'minimo de horas dedicadas: {minimo}')
        
# funcion para generar un informe en (TXT)
def generarInformeTareas(listaTareas):
    if not listaTareas:
        print('no hay tareas para generar informe')
        return
    
    #abrir un archivo txt para escribir un informe
    with open("informe_tareas.txt", "w") as archivo:
        #escribir los detalles de la tarea en el archivo
        for tarea in listaTareas:
            archivo.write(f"\n Nombre: {tarea.nombre}")
            archivo.write(f'Nombre: {tarea.nombre}')
            archivo.write(f'Fecha Limite: {tarea.fechaLimite.strftime("%d/%m/%Y")}')
            archivo.write(f'Categorias: {tarea.categorias}')
            archivo.write(f'Horas dedicadas: {tarea.horasDedicadas}')
            archivo.write("\n")
    print("¡informe generado exitosamente!")
    
# crear una funcion para el menu 
def menu():
    listaTareas = []
    while True:
        print("\nMenu de opciones:")
        print("1. Agregar tarea")
        print("2. Visualizar tareas")
        print("3. Analizar tareas")
        print("4. Generar informe de tareas")
        print("5. Salir")
        
        opcion = int(input("Ingrese una opcion: "))
        
        if opcion == "1":
            agregarTarea(listaTareas)
        elif opcion == "2":
            visualizarTareas(listaTareas)
        elif opcion == "3":
            analizarTareas(listaTareas)
        elif opcion == "4":
            generarInformeTareas(listaTareas)
        elif opcion == "5":
            print("¡Gracias por utilizar el programa!")
            break
        else:
            print("Opcion no valida")
            

if __name__ == "__main__":
    menu()