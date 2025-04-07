# Programa para calcular salario neto
salario_bruto = float(input("Ingrese el salario bruto del empleado: "))
impuesto = salario_bruto * 0.10
seguro = salario_bruto * 0.05
pension = salario_bruto * 0.03
descuentos = impuesto + seguro + pension
salario_neto = salario_bruto - descuentos
print(f"Salario bruto: ${salario_bruto}")
print(f"Descuentos totales: ${descuentos}")
print(f"Salario neto: ${salario_neto}")