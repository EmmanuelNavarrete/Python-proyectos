#Programa que saque el volumen de diferentes figuras
# esfera, cilindro, cubo, piramide, tetraedro

menu = """
elige una opcion:
1. Esfera
2. Cilindro
3. Cubo
4. Piramide
5. Tetraedro
6. Salir
"""
volumen = 0
opcion = int(input(menu))
while opcion != 6:
    if opcion == 1:
        radio = float(input("Ingrese el radio de la esfera: "))
        volumen = (4/3) * 3.14 * radio * radio * radio
        print("El volumen de la esfera es: " + str(volumen))
    elif opcion == 2:
        radio = float(input("Ingrese el radio del cilindro: "))
        altura = float(input("Ingrese la altura del cilindro: "))
        volumen = 3.14 * radio * radio * altura
        print("El volumen del cilindro es: " + str(volumen))
    elif opcion == 3:
        lado = float(input("Ingrese el lado del cubo: "))
        volumen = lado * lado * lado
        print("El volumen del cubo es: " + str(volumen))
    elif opcion == 4:
        base = float(input("Ingrese la base de la piramide: "))
        altura = float(input("Ingrese la altura de la piramide: "))
        volumen = (1/3) * base * altura
        print("El volumen de la piramide es: " + str(volumen))
    elif opcion == 5:
        base = float(input("Ingrese la base del tetraedro: "))
        altura = float(input("Ingrese la altura del tetraedro: "))
        volumen = (1/3) * base * altura
        print("El volumen del tetraedro es: " + str(volumen))
    else:
        print("Opcion no valida")
    opcion = int(input(menu))
    