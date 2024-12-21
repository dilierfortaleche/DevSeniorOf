# Crea un programa que pida al usuario su calificación (entre 0 y 100). Dependiendo del valor ingresado, el programa debe mostrar si el estudiante ha aprobado (60 o más) o ha reprobado (menos de 60). Usa condicionales para determinar el resultado.

# Pedir al usuario que ingrese la calificación
calificacion = float(input("Ingresa tu calificación (entre 0 y 100): "))


# Determinar si el estudiante ha aprobado o ha reprobado
while calificacion < 0:
    print("La calificación no puede ser menor que 0. Por favor, intenta de nuevo")
    calificacion = float(input("Ingresa tu calificación (entre 0 y 100): "))
if calificacion > 100:
    print("La calificación debe estar entre 0 y 100")
elif calificacion < 60:
    print(f"Lo siento. Tu calificación es de {calificacion}, has reprobado")
else:
    print(f"Felicidades, Tu calificación es de {calificacion} has aprobado!")
