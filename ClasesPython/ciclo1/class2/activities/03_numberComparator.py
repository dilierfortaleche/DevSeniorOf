# Escribe un programa que solicite dos números al usuario y determine si el primer número es mayor, menor o igual al segundo. Muestra el resultado en pantalla usando operadores relacionales.

#solicitar al usuario que ingrese los numeros
num1 = float(input("Ingresa el primer número: "))
num2 = float(input("Ingresa el segundo número: "))

#realizr las comparaciones
if num1 > num2:
    print(f"{num1} es mayor que {num2}")
elif num1 < num2:
    print(f"{num1} es menor que {num2}")
else:
    print(f"{num1} es igual que {num2}")