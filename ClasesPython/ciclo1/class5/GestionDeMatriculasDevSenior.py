estudiantes = []
cursos = ['Java', 'Python']
docentes = []
horarios = []

#funciom para matricular estudiantes
def matricularEstudiante():
    nombre = input('Ingrese el nombre del estudiante: ')
    print('selecione curso a matricular (Java o Python): ')
    for i, curso in enumerate(cursos):
        print(f'{i+1}: {curso}')
    
    cursoSeleccionado = int(input('Ingrese el numero del curso: '))
    if cursoSeleccionado > 0 and cursoSeleccionado <= len(cursos):
        curso = cursos[cursoSeleccionado - 1]
        estudiante = {'nombre': nombre, 'curso': curso}
        estudiantes.append(estudiante)
        print(f'Estudiante: {nombre},  matriculado en el curso {curso}')
    else:
        print(f'Opcion de curso no valida, recuerde que solo hay {len(cursos)} cursos')
        
#funcion para asignar un docentes a un curso
def asignarDocente():
    print('seleccionar el curso al que desea asisgnar el docente')
    for i, curso in enumerate(cursos):
        print(f'{i+1}: {curso}')
        
    cursoSeleccionado = int(input('Ingrese el numero del curso: '))
    
    if cursoSeleccionado > 0 and cursoSeleccionado <= len(cursos):
        curso = cursos[cursoSeleccionado - 1]
        nombreDocente = input('Ingrese el nombre del docente: ')
        docente = {'nombre': nombreDocente, 'curso': curso}
        docentes.append(docente)
        print(f'Docente: {nombreDocente},  asignado en el curso {curso}')
    else:
        print(f'Opcion de curso no valida, recuerde que solo hay {len(cursos)} cursos')
        
#funcion para asignar un horario a un curso
def asignarHorario():
    print('seleccionar el curso al que desea asisgnar el horario')
    for i, curso in enumerate(cursos):
        print(f'{i+1}: {curso}')
        
    cursoSeleccionado = int(input('Ingrese el numero del curso: '))
    
    if cursoSeleccionado > 0 and cursoSeleccionado <= len(cursos):
        curso = cursos[cursoSeleccionado - 1]
        dias = input('Ingrese los dias de clases ( ej: martes y jueves): ')
        hora = input('Ingrese la hora de calases ( ej: 6 pm): ')
        horario = {'curso': curso, 'dias': dias, 'hora': hora}
        horarios.append(horario)
        print(f'Horario asignado al curso: {curso}: {dias} a las {hora}')
    else:
        print(f'Opcion de curso no valida, recuerde que solo hay {len(cursos)} cursos')
        

def mostarEstudiantes():
    if estudiantes:
        print('lista de Estudiantes matriculados')
        for estudiante in estudiantes:
            print(f"Estudiante: {estudiante['nombre']}, curso: {estudiante['curso']}")
    else:
        print('No hay estudiantes matriculados')
        
def mostarDocentes():
    if docentes:
        print('lista de docentes')
        for docente in docentes:
            print(f"Estudiante: {docente['nombre']}, curso: {docentes['curso']}")
    else:
        print('No hay docentes asignados')
        
def mostarHorarios():
    if horarios:
        print('lista de Estudiantes matriculados')
        for horario in horarios:
            print(f"Curso: {horario['curso']}, Dias: {horario['dias']}, Hora: {horario['hora']}")
    else:
        print('No hay no hay horarios asignados')
        

while True:
    print(' ---Sistema de matricula Dev Senior---')
    print('1. Matricular estudiante')
    print('2. Asignar docente a un curso')
    print('3. Asignar horario a un curso')
    print('4. Mostrar la lista de estudiantes matriculados')
    print('5. Mostrar la lista de docentes asignados')
    print('6. Mostrar horarios de los cursos')
    print('7. Salir')
    
    opcion = int(input('Ingrese una opcion: '))
    
    if opcion == 1:
        matricularEstudiante()
    elif opcion == 2:
        asignarDocente()
    elif opcion == 3:
        asignarHorario()
    elif opcion == 4:
        mostarEstudiantes()
    elif opcion == 5:
        mostarDocentes()
    elif opcion == 6:
        mostarHorarios()
    elif opcion == 7:
        print('Gracias por usar el sistema de matricula Dev Senior')
        break
    else:
        print('Opcion invalida. intente de nuevo Ingresar entre (1-7)')