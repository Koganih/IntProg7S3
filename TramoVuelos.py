tramo1 = float(input("Ingrese la duración del primer tramo (en horas): "))
escala1 = float(input("Ingrese la duración de la primera escala (en horas): "))
tramo2 = float(input("Ingrese la duración del segundo tramo (en horas): "))
escala2 = float(input("Ingrese la duración de la segunda escala (en horas): "))
tramo3 = float(input("Ingrese la duración del tercer tramo (en horas): "))
tiempo_total = tramo1 + escala1 + tramo2 + escala2 + tramo3
print(f"El tiempo total del viaje es: {tiempo_total} horas")