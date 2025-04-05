Algoritmo ConversionTiempo
    Definir total_segundos, horas, minutos, segundos, resto Como Real
    Escribir "Ingrese la cantidad total de segundos: "
    Leer total_segundos
    horas = redon(total_segundos / 3600)
    resto = total_segundos - (horas * 3600)
    minutos = redon(resto / 60)
    segundos = resto - (minutos * 60)
    Escribir "Horas: ", horas
    Escribir "Minutos: ", minutos
    Escribir "Segundos: ", segundos
FinAlgoritmo