#codificacion camelCase
# 1.0 = Float, 35= int, "jhoan" = str

ventasTotales = 0.0

#solucion a los numeros negativos e ingresar numero de productos a gestionar
while True:
    numProducto = int(input("Ingrese el número de productos a gestionar: "))
    if numProducto > 0:
        break
    else:
        print("Por favor, ingrese un número mayor a 0.")

#listas para almacenar la informacion
nombres = []
precios = []
cantidades = []

print('ingrese inicial del producto a la tienda')
for i in range(numProducto):
    print(f'producto {i+1}: ')
    nombre= input('ingrese el nombre del producto: ').lower()
    nombres.append(nombre)
    
    while True:
        precio = float(input('Digite el precio del producto: '))
        if precio > 0:
            break
        else:
            print("Por favor, ingrese un precio mayor a 0.")
    precios.append(precio)
    
    while True:
        cantidad = int(input('Digite la cantidad del producto: '))
        if cantidad > 0:
            break
        else:
            print("Por favor, ingrese una cantidad mayor a 0.")
    cantidades.append(cantidad)
    

#ciclo principal
while True:
    print('\n -----MENU DROGERIA----')
    print('1. Vender Producto')
    print('2. Mostar Inventario')
    print('3. Mostrar Ventas Totales')
    print('4. Salir')
    
    opcion = int(input('Ingrese una opcion: '))
    
    if opcion == 1:
        print('\nVender Producto')
        nombreVenta = input('ingrese el nombre del producto a vender: ').lower()
        cantidadVender = int(input('ingrese la cantidad a vender: '))
        productoEncontrado = False
        
        for i in range(len(nombres)):
            if nombres[i] == nombreVenta:
                productoEncontrado = True
                if cantidadVender <= cantidades[i]:
                    totalVenta = cantidadVender * precios[i]
                    ventasTotales += totalVenta
                    cantidades[i] -= cantidadVender
                    
                    print(f'venta realizada, total de esta venta ${totalVenta:.2f}')
                    print(f'quedan {cantidades[1]}unidades de {nombres[i]} en el inventario.')
                else:
                    print(f'cantidad insuficiente en el inventario, ya que en sta¿ock solo tenemos {cantidades[i]}')
                    break
        
        if not productoEncontrado:
            print('producto no encontrado en el inventario')
            
    elif opcion == 2:
        print('\nInventario de productos')
        for i in range(len(nombres)):
            print(f'producto {i+1}: {nombres[i].capitalize()}, precio: ${precios[i]:2f}, cantidad: {cantidades[i]}')
            
    elif opcion == 3:
        print(f'\nVentas totales acumuladas: ${ventasTotales:.2f}')
        
    elif opcion == 4:
        print('gracias por usar el sistema de gestion drogueria dev senior')
        break
    
    else:
            
        print('opcion invalida. ingresar entre (1-4)')