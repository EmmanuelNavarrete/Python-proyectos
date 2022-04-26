#Palabra palindromo
reversa = []
palabra = input("Ingrese una palabra: ")
for i in range(len(palabra)):
    reversa.append(palabra[len(palabra)-1-i])
if palabra == "".join(reversa):
    print("Es un palindromo")
else:
    print("No es un palindromo")
    