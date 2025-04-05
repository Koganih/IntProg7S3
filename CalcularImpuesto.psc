Algoritmo CalcularImpuesto
	// Calcular el impuesto a pagar de un producto
	Definir precio, porc_impuesto, valor_imp, total_pago, valor Como Real
	Escribir "dime el precio del producto: "
	Leer precio
	Escribir "dime el porcentaje de impuesto a aplicar"
	Leer porc_impuesto
	porc_impuesto = porc_impuesto / 100
	valor_imp = precio * porc_impuesto
	total_pago = precio + valor_imp
	Escribir "Precio: ", precio
	Escribir "Porcentaje de impuesto: " porc_impuesto 
	escribir "Valor de impuesto: ", valor_imp 
	escribir "total de pago: ", total_pago
FinAlgoritmo
