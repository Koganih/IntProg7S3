precio_original = float(input("Ingrese el precio original del producto: "))
porc_descuento = float(input("Ingrese el porcentaje de descuento: "))
descuento = (precio_original * porc_descuento) / 100
precio_desc = precio_original - descuento
porc_iva = float(input("Ingrese el porcentaje de IVA: "))
iva = (precio_desc * porc_iva) / 100
precio_final = precio_desc + iva
print(f"Precio original: C${precio_original}")
print(f"Descuento aplicado: C${descuento}")
print(f"Precio con descuento: C${precio_desc}")
print(f"IVA calculado: C${iva}")
print(f"Precio final: C${precio_final}")