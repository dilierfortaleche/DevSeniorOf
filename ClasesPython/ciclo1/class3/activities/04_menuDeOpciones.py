# Crea un programa que muestre un menú de opciones simples (por ejemplo, "1. Saludar", "2. Despedirse", "3. Salir") y permita al usuario seleccionar una opción. Dependiendo de la opción, el programa debe ejecutar una acción específica o salir del bucle si el usuario elige "Salir". Usa un bucle while para mostrar el menú hasta que el usuario decida salir.

while True:
    print("1. Saludar")
    print("2. Despedirse")
    print("3. Salir")
    opcion = int(input("Ingrese una opción: "))
    if opcion == 1:
        print("Hola, ¿cómo estás?")
    elif opcion == 2:
        print("Adiós, que tengas un buen día.")
    elif opcion == 3:
        break
    else:
        print("Opción no válida. Por favor, intente de nuevo.")
