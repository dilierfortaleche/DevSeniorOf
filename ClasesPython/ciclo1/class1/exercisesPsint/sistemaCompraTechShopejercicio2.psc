Algoritmo sistemaCompraTechShop
	
	Escribir  "sistema de compras TechShop"
	
	Definir  usuarioValido, contrasenaValida Como Logico
	Definir  intentosLogin,intentosPagos, descuentos Como Entero
	Definir totalCompra, totalFinal, precioProducto, cantidadProducto, subTotal Como Real
	Definir respuestaPago Como Cadena
	
	//simulacion de credenciales
	usuarioValido <- Falso
	contrasenaValida <- Falso
	intentosLogin <- 0
	
	Mientras intentosLogin < 3 y (usuarioValido = Falso O contrasenaValida = Falso) Hacer
		Escribir "ingrese su nombre de usuario"
		Leer  nombreUsuario
		Escribir  "ingrese contraseña"
		Leer contrasena
		
		//verificar los credenciales
		Si  nombreUsuario = "cliente" Y contrasena = "1234" Entonces
			usuarioValido <- Verdadero
			contrasenaValida<- Verdadero
			Escribir  "inicio de sesion exitoso"
		SiNo
			intentosLogin <- intentosLogin + 1
			Si intentosLogin < 3 Entonces
				Escribir  "credencial incorrecta, intente de nuevo"
			SiNo
				Escribir "acceso bloqueado por demaciados intentos fallidos"
			FinSi
		FinSi
	FinMientras
	
	
	//selecion de productos
	totalCompra <- 0
	cantidadProducto<- 0
	precioProducto <- 0
	subTotal <- 0
	
	Repetir
		Escribir "ingrese el presio del producto(0 para finalizar)"
		Leer precioProducto
		Si precioProducto > 0 Entonces
			Escribir "ingrese la cantidad de producto: "
			Leer  cantidadProducto
			
			//calcular subtotal y agregalo al total
			subTotal <- precioProducto * cantidadProducto
			totalCompra <- totalCompra + subTotal
			Escribir ""
			
		FinSi
	Hasta Que 
	
FinAlgoritmo
