# Averiguar si el año es bisiesto
year = int(input("ingrese un año: "))

if year % 4 == 0 and year % 100 != 0 or year % 400 == 0:
    print(f"El año {year} es bisiesto")
else: print(f"El año {year} NO es bisiesto")