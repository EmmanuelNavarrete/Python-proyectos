#Programa que imprima la serie de Fibonacci
numero = int(input("Ingrese un numero: "))
fibonacci = [0, 1]
for i in range(2, numero):
    fibonacci.append(fibonacci[i-1] + fibonacci[i-2])
print(fibonacci)
