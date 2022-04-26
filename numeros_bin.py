#Bumero binario a decimal
binario = input("Ingrese un numero binario: ")
decimal = 0
for i in range(len(binario)):
    decimal += int(binario[i]) * 2**(len(binario)-1-i)
print(f"El numero binario {binario} en decimal es: {decimal}")

#Numero decimal a binario
decimal = int(input("Ingrese un numero decimal: "))
binario = ""
while decimal > 0:
    binario = str(decimal % 2) + binario
    decimal = decimal // 2
print(f"El numero decimal {decimal} en binario es: {binario}")
