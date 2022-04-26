#Programa que imprima el factorial de un numero
numero = int(input("Ingrese un numero: "))
factorial = 1
for i in range(1, numero+1):
    factorial = factorial * i
print(f"El factorial de {numero} es: {factorial}")
