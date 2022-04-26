#crear un programa que diga si es primo o no
numero = int(input("Ingrese un numero: "))
for i in range(2, numero):
    if numero % i == 0:
        print("El numero no es primo")
        break
else:
    print("El numero es primo")
