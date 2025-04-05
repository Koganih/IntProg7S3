Algoritmo CalculoTiempoViaje
    Definir tramo1, escala1, tramo2, escala2, tramo3, tiempo_total Como Real
    Escribir "Ingrese la duración del primer tramo (en horas): "
    Leer tramo1
    Escribir "Ingrese la duración de la primera escala (en horas): "
    Leer escala1
    Escribir "Ingrese la duración del segundo tramo (en horas): "
    Leer tramo2
    Escribir "Ingrese la duración de la segunda escala (en horas): "
    Leer escala2
    Escribir "Ingrese la duración del tercer tramo (en horas): "
    Leer tramo3
    tiempo_total = tramo1 + escala1 + tramo2 + escala2 + tramo3
    Escribir "El tiempo total del viaje es: ", tiempo_total, " horas"
FinAlgoritmo