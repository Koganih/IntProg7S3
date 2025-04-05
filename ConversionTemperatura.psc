// Algoritmo para convertir temperatura de Fahrenheit a Celsius y Kelvin
	Algoritmo ConversionTemperatura
	Definir fahrenheit, celsius, kelvin Como Real
	Escribir "Ingrese la temperatura en grados Fahrenheit: "
	Leer fahrenheit
	celsius = (fahrenheit - 32) * 5 / 9
	kelvin = celsius + 273.15
	Escribir "Temperatura en Celsius: ", celsius, " °C"
	Escribir "Temperatura en Kelvin: ", kelvin, " K"
FinAlgoritmo