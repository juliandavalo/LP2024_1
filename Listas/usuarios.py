

def main():
    nombres = []
    for i in range(5):
        nombre = input("Ingrese un nombre: ")
        nombres.append(nombre)

    print(f"La lista original fue: {nombres}")
    
    # pregunta si desea eliminar un nombre
    eliminar = input("Desea eliminar un nombre? (s/n): ")
    if eliminar.lower() == "s":
        nombre_eliminar = input("Ingrese el nombre a eliminar: ")
        if nombre_eliminar in nombres:
            nombres.remove(nombre_eliminar)
            print(f"La lista ahora es: {nombres}")
        else:
            print(f"El nombre {nombre_eliminar} no esta en la lista")
    
    # pregunta si desea adicionar un nombre
    adiciconar = input("Desea adicionar un nombre? (s/n): ")
    if adiciconar.lower() == "s":
        nombre_adicionar = input("ingrese el nombre a adicionar: ")
        nombres.insert(0, nombre_adicionar)
        print(f"la lista ahora es: {nombres}")
        
    # Mostrar el tamaño de la lista y los nombres en posicion impares
    print(f"El tamaño de la lista es: {len(nombres)}")
    print(f"Los nombres en posicion impares son: {nombres[1::2]}")

if __name__ == "__main__":
    main()
