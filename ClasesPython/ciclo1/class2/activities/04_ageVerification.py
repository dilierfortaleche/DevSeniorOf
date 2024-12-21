# Crea un programa que pida la edad del usuario y verifique si es mayor de edad (18 años o más). Usa operadores lógicos para determinar si la persona puede votar o no.

#pedir al usuario que ingrese la edad
edad = int(input("Ingresa tu edad: "))

#verificar si la persona es mayor de edad
if edad >= 18:
    print("Es mayor de edad y puede votar")
else:
    print("Es menor de edad no puede votar")