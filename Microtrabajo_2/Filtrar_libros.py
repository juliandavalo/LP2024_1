
import Inventario_libros as Inventario_libros
from functools import reduce

# imprimo la lista que hay en el inventario de libros
print(f"\nLista de libros: \n{Inventario_libros.lista}")

# Filtro la lista de libros de franz kafka
libros_de_Franz_Kafka = list(filter( lambda nombre: nombre [1] == 'Franz Kafka', Inventario_libros.lista)) 
print(f"\nLibros de Franz Kafka:\n {libros_de_Franz_Kafka}")

# Calculo la cantidad de libros en el inventario de libros
total_libros = reduce( lambda a, _: a + 1, Inventario_libros.lista,0)
print(f"\nTotal libros en el inventario:\n {total_libros}")

# Funcion para transformar la lista de tuplas en un diccionario
def tuplas_a_diccionario(lista):
    diccionario_libros = {}

    for libro, autor, anio in lista:
        diccionario_libro = {"autor": autor, "anio": anio}
        diccionario_libros[libro] = diccionario_libro

    return diccionario_libros

# Llamo la función para transformar la lista de tuplas a un diccionario
diccionario_completo = tuplas_a_diccionario(Inventario_libros.lista)
print(f"\nInventario convertido a diccionario:\n {diccionario_completo}\n\n")