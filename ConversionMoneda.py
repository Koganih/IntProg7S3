dolares = float(input("Ingrese la cantidad en dólares: "))
tasa_euro = 0.92    
tasa_libra = 0.79   
tasa_yen = 151.61   
euros = dolares * tasa_euro
libras = dolares * tasa_libra
yenes = dolares * tasa_yen
print(f"Cantidad en dólares: ${dolares}")
print(f"Cantidad en euros: €{euros}")
print(f"Cantidad en libras: £{libras}")
print(f"Cantidad en yenes: ¥{yenes}")