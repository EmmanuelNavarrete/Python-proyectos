#Calcular el IMC de una persona
peso = float(input("¿ Cuanto pesa ? "))
altura = float(input("¿ Cuanto mide ? "))
imc = peso / (altura * altura)
print(f"Tu IMC es: {imc}")
if imc < 18.5:
    print("Tienes bajo peso")
elif imc >= 18.5 and imc <= 24.9:
    print("Tienes peso normal")
elif imc >= 25 and imc <= 29.9:
    print("Tienes sobrepeso")
elif imc >= 30 and imc <= 34.9:
    print("Tienes obesidad tipo 1")
elif imc >= 35 and imc <= 39.9:
    print("Tienes obesidad tipo 2")
elif imc >= 40:
    print("Tienes obesidad tipo 3")
else:
    print("Opcion no valida")

