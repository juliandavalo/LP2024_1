# Asigna un acalificacion de acuerdo al promedio
calificacion = int(input("Ingrese el promedio obtenido en la prueba: "))
if  90 <= calificacion <= 100:
    print("Su calificacion es: A")
if  80 <= calificacion < 90:
    print("Su calificacion es: B")
if  70 <= calificacion < 80:
    print("Su calificacion es: C")
if  60 <= calificacion < 70:
    print("Su calificacion es: D")
if  calificacion < 60:
    print("Su calificacion es: E")