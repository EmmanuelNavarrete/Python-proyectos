#Adivina el numero entre el 1 y el 20
import  random
num_encontrar = int(input("Ingrese un numero: "))
random_num = random.randint(1, 20)
intentos = 0
while num_encontrar != random_num:
    intentos = intentos + 1
    num_encontrar = int(input("Ingrese un numero: "))
    if num_encontrar == random_num:
        print("Felicidades, adivinaste el numero")
    elif num_encontrar > random_num:
        print("El numero es menor")
    else:
        print("El numero es mayor")

        print(f"El numero de intentos fue: {intentos}")