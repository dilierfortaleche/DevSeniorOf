# Crea un programa que convierta una medida en metros a centímetros y milímetros. El programa debe pedir al usuario que ingrese una longitud en metros y luego mostrar el resultado en las dos unidades.


#solicitar el usuario que ingrese una longitud en metros

metros = float(input("Ingrese una longitud en metros: "))

#realizar las conversiones

centimetros = metros * 100
milimetros = metros * 1000

#mostrar los resultados

print(f"{metros} metros son {centimetros} centimetros y {milimetros} milimetros")