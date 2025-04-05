Algoritmo CalculoSalario
    Definir salario_bruto, impuesto, seguro, pension, descuentos, salario_neto Como Real
    Escribir "Ingrese el salario bruto del empleado: "
    Leer salario_bruto
    impuesto = salario_bruto * 0.10
    seguro = salario_bruto * 0.05
    pension = salario_bruto * 0.03
    descuentos = impuesto + seguro + pension
    salario_neto = salario_bruto - descuentos
    Escribir "Salario bruto: $", salario_bruto
    Escribir "Descuentos totales: $", descuentos
    Escribir "Salario neto: $", salario_neto
FinAlgoritmo