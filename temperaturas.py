#Conversor de temepraturas
def celcius_to_fahrenheit(celcius):
    fahrenheit = celcius * 9/5 + 32
    return fahrenheit
def fahrenheit_to_celcius(fahrenheit):
    celcius = (fahrenheit - 32) * 5/9
    return celcius
def kelvin_to_celcius(kelvin):
    celcius = kelvin - 273.15
    return celcius
def celcius_to_kelvin(celcius):
    kelvin = celcius + 273.15
    return kelvin
def kelvin_to_fahrenheit(kelvin):
    fahrenheit = (kelvin - 273.15) * 9/5 + 32
    return fahrenheit
def fahrenheit_to_kelvin(fahrenheit):
    kelvin = (fahrenheit - 32) * 5/9 + 273.15
    return kelvin

menu = """
Bienvenido al conversor de temperaturas
1 - Celsius a Fahrenheit
2 - Fahrenheit a Celsius
3 - Kelvin a Celsius
4 - Celsius a Kelvin
5 - Kelvin a Fahrenheit
6 - Fahrenheit a Kelvin
7 - Salir
Elija una opcion: """
opcion = int(input(menu))
while opcion != 7:
    if opcion == 1:
        celcius = float(input("Ingrese la temperatura en Celsius: "))
        fahrenheit = celcius_to_fahrenheit(celcius)
        print("La temperatura en Fahrenheit es: " + str(fahrenheit))
    elif opcion == 2:
        fahrenheit = float(input("Ingrese la temperatura en Fahrenheit: "))
        celcius = fahrenheit_to_celcius(fahrenheit)
        print("La temperatura en Celsius es: " + str(celcius))
    elif opcion == 3:
        kelvin = float(input("Ingrese la temperatura en Kelvin: "))
        celcius = kelvin_to_celcius(kelvin)
        print("La temperatura en Celsius es: " + str(celcius))
    elif opcion == 4:
        celcius = float(input("Ingrese la temperatura en Celsius: "))
        kelvin = celcius_to_kelvin(celcius)
        print("La temperatura en Kelvin es: " + str(kelvin))
    elif opcion == 5:
        kelvin = float(input("Ingrese la temperatura en Kelvin: "))
        fahrenheit = kelvin_to_fahrenheit(kelvin)
        print("La temperatura en Fahrenheit es: " + str(fahrenheit))
    elif opcion == 6:
        fahrenheit = float(input("Ingrese la temperatura en Fahrenheit: "))
        kelvin = fahrenheit_to_kelvin(fahrenheit)
        print("La temperatura en Kelvin es: " + str(kelvin))
    else:
        print("Opcion no valida")
    opcion = int(input(menu))
print("Gracias por usar el conversor de temperaturas")