Algoritmo  verificarContraseña
	
	Definir contraseñaCorrecta Como Cadena
	Definir  contraseñaIngresada Como Cadena
	Definir Intentos Como Entero
	Definir accesoPermitido Como Logico
	
	//contaseña Correcta
	contraseñaCorrecta = "1234"
	Intentos <- 0
	
	Mientras intentos < 3 y accesoPermitido = falso Hacer
		Escribir  "ingrese su contraseña: "
		Leer  contraseñaIngresada
		
		Si contraseñaIngresada = contraseñaCorrecta Entonces
			accesoPermitido = Verdadero
		SiNo
			intentos <- intentos + 1
			Escribir  "contraseña incorrecta. Intentos", intentos, "de 3."
		Finsi
	FinMientras
	si accesoPermitido = falsp Entonces
		Escribir  "cuenta suspendida temporalmente. Ha excedido el numero de intentos"
	SiNo
		Escribir  "Acceso permitido al sistema"
	FinSi
FinAlgoritmo
	