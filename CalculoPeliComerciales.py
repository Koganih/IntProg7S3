duracion_pelicula = float(input("Ingrese la duración de la película en minutos: "))
com_previos = float(input("Ingrese la duración de los comerciales previos en minutos: "))
cant_pausas = float(input("Ingrese la cantidad de pausas comerciales: "))
dur_pausa = float(input("Ingrese la duración de cada pausa comercial en minutos: "))
com_durante = cant_pausas * dur_pausa
duracion_total = duracion_pelicula + com_previos + com_durante
print(f"Duración original de la película: {duracion_pelicula} minutos")
print(f"Duración de los comerciales totales: {com_previos + com_durante} minutos")
print(f"Tiempo total de la proyección: {duracion_total} minutos")