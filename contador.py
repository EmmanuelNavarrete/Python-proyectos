#Contador de Vocales
palabra = input("Ingrese una palabra: ")
contador = 0
for letra in palabra:
    if letra == "a" or letra == "e" or letra == "i" or letra == "o" or letra == "u":
        contador += 1
print("La palabra tiene", contador, "vocales")
#numero de letras de la palabra
palabra = input("Ingrese una palabra: ")
contador = 0
for letra in palabra:
    contador += 1
print("La palabra tiene", contador, "letras")
#numero de consonantes de la palabra
palabra = input("Ingrese una palabra: ")
contador = 0
for letra in palabra:
    if letra != "a" and letra != "e" and letra != "i" and letra != "o" and letra != "u":
        contador += 1
print("La palabra tiene", contador, "consonantes")