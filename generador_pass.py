#generador de contraseñas
import random
letras = "abcdefghijklmnopqrstuvwxyz"
mayusculas = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
numeros = "0123456789"
caracteres = "!@#$%^&*()_+-=[]{}|;:,./<>?\'"

#digitos = int(input("Cuantos digitos desea que tenga su contraseña: "))

'''for i in range(digitos):
    caracter = random.choice(letras + mayusculas + numeros + caracteres)
    print(caracter, end="")'''
menu = '''
 Elija una opcion:
 1. Contraseña con letras
 2. Contraseña con letras mayusculas
 3. Contraseña con letras mayusculas y minusculas
 4. Contraseña con letras mayusculas, minusculas y numeros
 5. Contraseña con letras mayusculas, minusculas, numeros y caracteres especiales
 6. Salir
'''
opcion = int(input(menu))
while opcion != 6:
    if opcion == 1:
        digitos = int(input("Cuantos digitos desea que tenga su contraseña: "))
        for i in range(digitos):
            caracter = random.choice(letras)
            print(caracter, end="")
    elif opcion == 2:
        digitos = int(input("Cuantos digitos desea que tenga su contraseña: "))
        for i in range(digitos):
            caracter = random.choice(mayusculas)
            print(caracter, end="")
    elif opcion == 3:
        digitos = int(input("Cuantos digitos desea que tenga su contraseña: "))
        for i in range(digitos):
            caracter = random.choice(letras + mayusculas)
            print(caracter, end="")
    elif opcion == 4:
        digitos = int(input("Cuantos digitos desea que tenga su contraseña: "))
        for i in range(digitos):
            caracter = random.choice(letras + mayusculas + numeros)
            print(caracter, end="")
    elif opcion == 5:
        digitos = int(input("Cuantos digitos desea que tenga su contraseña: "))
        for i in range(digitos):
            caracter = random.choice(letras + mayusculas + numeros + caracteres)
            print(caracter, end="")
    else:
        print("Opcion no valida")
    opcion = int(input(menu))
print("Gracias por usar el generador de contraseñas")
