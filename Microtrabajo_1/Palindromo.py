# ingresar cadena de texto y determine si es un palíndromo


def palindromo(cadena):
    
    cadena = cadena.lower()
    cadena = cadena.replace(" ", "")
    cadena = cadena.replace(",", "")
    cadena = cadena.replace(".", "")
    cadena = cadena.replace(";", "")
    
    a = 0
    b = len(cadena) - 1

    for i in range(0, len(cadena)):
        if cadena[a] == cadena[b]:
            a += 1
            b -= 1
             
        else:
            return False
        
    return True   

cadena = input("ingese una cadena: ")
if len(cadena) >= 3:      
    if palindromo(cadena):
        print(f"La cadena {cadena} es un palindromo")     
    else:
        print(f"La cadena {cadena} NO es un palindromo") 

else:
    print(f"La cadena {cadena} es menor de 3 letras")