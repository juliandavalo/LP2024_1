# Solicitar la temperatura del invernadero
temperatura = float(input("Ingrese cual es la temperatura del invernadero: "))

# Aplicamos las reglas para el control de temperatura
if temperatura > 30.0:
    print("Activando sistema de enfriamiento")
elif temperatura >= 18 and temperatura <= 30:
    print("Temperatura optima. Sin cambios")
else:
    print("Activando sistema de calefaccion")