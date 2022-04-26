#Conversor de pesos 
def conversor (tipo_pesos, valor_dolar):
    pesos = input("Cuantos pesos "+ tipo_pesos +" tienes ? ")    
    pesos = float(pesos)
    dolares = pesos / valor_dolar
    dolares = round(dolares, 2)
    print("Tienes $" + str(dolares) + " dolares")

menu = """
Bienvenido al converosor de monedas
1 - Pesos Colombianos
2 - Pesos Argentinos
3 - Pesos Mexicanos
4 - Pesos Uruguayos
5 - Pesos Bolivianos

Elige una opcion: """

opcion = int(input(menu))
if opcion == 1:
    conversor("colombianos", 3723.01)
elif opcion == 2:
    conversor("argentinos", 113.90)
elif opcion == 3:
    conversor("mexicanos", 19.07)
elif opcion == 4:
    conversor("uruguayos", 41.68)
elif opcion == 5:
    conversor("bolivianos", 6.87)
else:
    print("Opcion no valida")   
