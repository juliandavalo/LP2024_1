# Importa el módulo random para generar números aleatorios
import random  

# Define la tolerancia del 5% para las resistencias, usamos uniform para general el numero aleatorio en un rango 
tolerancia_resistencias = random.uniform(-0.05, 0.05)  


# Función para calcular la resistencia total del circuito
def calcular_resistencia_total(resistencias):
    return sum(resistencias) # sum se usa para sumar todos los elementos de la lista resistencias 

# Función para calcular la corriente del circuito usando la ley de Ohm
def calcular_corriente(voltaje, resistencia_total):
    return voltaje / resistencia_total  

#esta funcion coge la resistencia y le asigna su tolerancia
def simular_tolerancias(valor):
    variacion = valor * tolerancia_resistencias  # Simula la tolerancia de las resistencias aplicando un valor aleatorio
    return valor + variacion  # Devuelve el valor simulado de la resistencia

# aca definimos el valor de la corriente para convetir todo en su escala
def interpretar_valor_corriente(valor):
    # Función para interpretar y formatear el valor de la corriente en diferentes unidades (Amperios, miliAmperios, etc.)
    if valor >= 1e3:
        return f"{valor/1e3:.2f} KiloAmperios"
    elif valor >= 1:
        return f"{valor:.2f} Amperios"
    elif valor >= 1e-3:
        return f"{valor*1e3:.2f} miliAmperios"
    elif valor >= 1e-6:
        return f"{valor*1e6:.2f} microAmperios"
    elif valor >= 1e-9:
        return f"{valor*1e9:.2f} nanoAmperios"

# Función para interpretar y convertir el valor de la resistencia a Ohmios
def interpretar_valor_resistencia(valor):
    #si viene un numero acompañado de  K o k en la variable nos lo multiplica por  1000
    if valor[-1] == 'K' or valor[-1] == 'k':
        return float(valor[:-1]) * 1000
    #si viene un numero acompañado de  M en la variable nos lo multiplica por  1000000
    elif valor[-1] == 'M':
        return float(valor[:-1]) * 1000000
    #si el valor es un numero lo tome como un float
    elif valor.isdigit():
        return float(valor)
    # de lo contrario si viene un valor diferente me mande none 
        return None  

def formatear_valor_resistencia(valor):
    # Función para formatear el valor de la resistencia en diferentes unidades (Ohmios, Kiloohmios, etc.)
    if valor >= 1e6:
        return f"{valor/1e6:.2f} Megaohmios"
    elif valor >= 1e3:
        return f"{valor/1e3:.2f} Kiloohmios"
    elif valor >= 1:
        return f"{valor:.2f} Ohmios"
    elif valor >= 1e-6:
        return f"{valor*1e6:.2f} microohmios"
    elif valor >= 1e-3:
        return f"{valor*1e3:.2f} miliOhmios"
# Función para construir un circuito interactivo
def construir_circuito():
    # Solicita el voltaje de la fuente
    voltaje_fuente = float(input("Ingrese el valor de la fuente de voltaje (en voltios): "))  
    
    # Inicializa la representación visual del circuito
    circuito = ""  
    # Lista para almacenar los valores de resistencia
    resistencias = []  
    
    
    # Imprime el voltaje de la fuente inicial
    print(f"\n(V{voltaje_fuente}) -> ")  

    #Creo un ciclo
    while True:
        #Hago un Menu para el programa
        print("\nSeleccione una opción:")
        print("1. Agregar resistencia en serie.")
        print("2. Agregar resistencia en paralelo.")
        print("3. Cerrar circuito.")
        opcion = input("Seleccione una opción: ")  # Solicita al usuario una opción
        
        #Creo un codicional por la opcion digiada es la 1 ( Agregar resistencia en serie.)
        if opcion == '1':  
            #creo un ciclo para cuando el usuario el usuario digite un valor incorrecto de la resistencia
            while True:
                valor_resistencia = input("Ingrese el valor de la resistencia en serie (con sufijo K para kiloohmios o M para megaohmios): ")
                #asigno a valor_resistencia la respuesta de ejecutar 
                #la funcion interpretar_valor_resistencia  con lo que digito el usuario
                valor_resistencia = interpretar_valor_resistencia(valor_resistencia) # Convierte el valor a Ohmios
                # si es valor no es None sale del bucle o ciclo y entra al menu nuevamente
                if valor_resistencia is not None:
                    break  # Sale del bucle si el valor es válido
                # de lo contrario si es None me sale un mensaje para que digite un valor valido de la resistencia
                else:
                    print("Valor de resistencia no válido. Por favor, ingrese un valor válido.")
            #a circuito le sumo este string para seguir con el plano del circuitos que se muestra en pantalla
            circuito += f"|-RS{valor_resistencia}-| -> "  
            
            # Imprime el circuito actualizado
            print(f"\n(V{voltaje_fuente}) -> {circuito}") 
            # Agrega el valor de resistencia a la lista 
            resistencias.append(valor_resistencia)  

        elif opcion == '2':  # Si elige agregar resistencia en paralelo
            while True:
                valor_resistencia1 = input("Ingrese el valor de la primera resistencia en paralelo (con sufijo K para kiloohmios o M para megaohmios): ")
                valor_resistencia1 = interpretar_valor_resistencia(valor_resistencia1)
                if valor_resistencia1 is not None:
                    break
                else:
                    print("Valor de la primera resistencia no válido. Por favor, ingrese un valor válido.")

            while True:
                valor_resistencia2 = input("Ingrese el valor de la segunda resistencia en paralelo (con sufijo K para kiloohmios o M para megaohmios): ")
                valor_resistencia2 = interpretar_valor_resistencia(valor_resistencia2)
                if valor_resistencia2 is not None:
                    break
                else:
                    print("Valor de la segunda resistencia no válido. Por favor, ingrese un valor válido.")

            circuito += f"|-RP{valor_resistencia1}/{valor_resistencia2}-| "
            print(f"\n(V{voltaje_fuente}) -> {circuito}")
            #hacemos la formula para calcular al resistencia en paralelo
            Resistencia_Paralelo=(1/((1/valor_resistencia1)+(1/valor_resistencia2)))
            #se agrega a resistencias el valor calculado de Resistencia_Paralelo
            resistencias.extend([Resistencia_Paralelo])

        elif opcion == '3':  # Si elige cerrar el circuito
            # Simula las tolerancias de las resistencias y calcula la resistencia total y la corriente
            # con el for recorremos una por una las resistencias 
            # y se hace la simulacion de las tolerancia y se le da su nuevo valor
            resistencias_con_tolerancia = [simular_tolerancias(valor) for valor in resistencias]
            resistencia_total = calcular_resistencia_total(resistencias_con_tolerancia)
            corriente = calcular_corriente(voltaje_fuente, resistencia_total)
            corriente_formateada = interpretar_valor_corriente(corriente)
            print(resistencias)
            # Imprime el circuito final, la tolerancia, la corriente y la resistencia total formateada
            print(f"\n(V{voltaje_fuente}) -> {circuito} -> ----(GND)")
            print(f"\nTolerancia de las resistencias: {(tolerancia_resistencias*100):.2f}%")
            print(f"Corriente Resultante: {corriente_formateada}")
            print(f"Resistencia Total: {formatear_valor_resistencia(resistencia_total)}")
            break  # Sale del bucle

        else:
            print("Opción no válida. Por favor, seleccione una opción válida.")

construir_circuito()  # Llama a la función para comenzar la construcción del circuito#