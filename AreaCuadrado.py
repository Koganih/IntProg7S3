""" calcular area de un rectangulo """
LadoA = float(input("Ingrese lado del rectangulo"))
BaseA = float(input("ingrese base del rectangulo"))
Area = (LadoA * BaseA)
mult = (LadoA * 2) 
mult2 = (BaseA * 2)
perimetro = (mult + mult2)
print(f"el area del rectangulo es :", Area)
print(f"el perimetro del rectangulo es:", perimetro)