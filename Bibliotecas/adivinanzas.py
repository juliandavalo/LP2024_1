
#juego de adivinanza
# el programa genera un numeor aleatorio de 1 a 100

import random
def main():
    number = random.randint(1, 100)
    intentos = 5
    for i in ramge(intentos):
        num_user = int(input("adivina el numero: "))
        if num_user == number:
            print("felicidades, adivinaste el umero")
        elif num_user < number:
            print("el numero es mayor")
        else:
            print("el numero es menor")
    if num_user != number:
        print(f"perdiste, el numero era {number}")


#entry print


