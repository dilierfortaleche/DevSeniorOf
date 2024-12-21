# Escribe un programa que recorra los números del 1 al 20 e imprima si cada número es par o impar. Usa un bucle for para recorrer los números y condicionales para determinar si un número es par o impar.

for i in range(1, 21):
    if i % 2 == 0:
        print(f"{i} es par")
    else:
        print(f"{i} es impar")
