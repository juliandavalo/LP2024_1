

# create my first functions to calculate the area of a rectangle
def area_rectangle(length, width):
    """
    doctrings: this functions calculates the area of a rectangle
    """
    area = length * width
    return area
# llamo la funcion
length_user = float(input("Ingrese la altura del rectangulo: "))
width_user = float(input("Ingrese el ancho del rectangulo: "))

area_user = area_rectangle(length_user, width_user)

print(f"El area del rectangulo es: {area_user} con un largo de: {length_user}  y un ancho de: {width_user}")