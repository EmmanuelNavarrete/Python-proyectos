#Calcular el area de diferentes figuras
area = 0
menu = """
Bienvenido al calculador de area
1 - Cuadrado
2 - Triangulo
3 - Circulo
4 - Rombo
5 - Rectangulo
6 - Salir
Elija una opcion: """
opcion = int(input(menu))
while opcion != 6:
    if opcion == 1:
        lado = float(input("Ingrese el lado del cuadrado: "))
        area = lado * lado
        print("El area del cuadrado es: " + str(area))
    elif opcion == 2:
        base = float(input("Ingrese la base del triangulo: "))
        altura = float(input("Ingrese la altura del triangulo: "))
        area = (base * altura) / 2
        print("El area del triangulo es: " + str(area))
    elif opcion == 3:
        radio = float(input("Ingrese el radio del circulo: "))
        area = 3.14 * radio * radio
        print("El area del circulo es: " + str(area))
    elif opcion == 4:
        diagonal = float(input("Ingrese la diagonal del rombo: "))
        area = diagonal * diagonal
        print("El area del rombo es: " + str(area))
    elif opcion == 5:
        base = float(input("Ingrese la base del rectangulo: "))
        altura = float(input("Ingrese la altura del rectangulo: "))
        area = base * altura
        print("El area del rectangulo es: " + str(area))
    else:
        print("Opcion no valida")
    opcion = int(input(menu))
print("Gracias por usar el calculador de area")
