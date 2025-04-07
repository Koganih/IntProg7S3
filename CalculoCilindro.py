radio = float(input("Ingrese el radio del cilindro: "))
altura = float(input("Ingrese la altura del cilindro: "))
area_base = 3.14159 * radio * radio
volumen = area_base * altura
area_lateral = 2 * 3.14159 * radio * altura
area_superficial = area_lateral + (2 * area_base)
print(f"Radio: {radio}")
print(f"Altura: {altura}")
print(f"Volumen: {volumen}")
print(f"Área superficial: {area_superficial}")