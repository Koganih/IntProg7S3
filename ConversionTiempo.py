total_segundos = float(input("Ingrese la cantidad total de segundos: "))
horas = int(total_segundos // 3600)
resto = total_segundos - (horas * 3600)
minutos = int(resto // 60)
segundos = resto - (minutos * 60)
print(f"Horas: {horas}")
print(f"Minutos: {minutos}")
print(f"Segundos: {segundos}")