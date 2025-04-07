# Programa para convertir temperatura de Fahrenheit a Celsius y Kelvin
fahrenheit = float(input("Ingrese la temperatura en grados Fahrenheit: "))
celsius = (fahrenheit - 32) * 5 / 9
kelvin = celsius + 273.15
print(f"Temperatura en Celsius: {celsius} °C")
print(f"Temperatura en Kelvin: {kelvin} K")