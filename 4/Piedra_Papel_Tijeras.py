import random

print("""
   _____   _       _                    _                                           
  / ____| | |     (_)                  | |                                          
 | |      | |__    _   _ __       ___  | |__     __ _   _ __ ___      _ __    _   _ 
 | |      | '_ \  | | | '_ \     / __| | '_ \   / _` | | '_ ` _ \    | '_ \  | | | |
 | |____  | | | | | | | | | |   | (__  | | | | | (_| | | | | | | |   | |_) | | |_| |
  \_____| |_| |_| |_| |_| |_|    \___| |_| |_|  \__,_| |_| |_| |_|   | .__/   \__,_|
                                                                     | |            
                                                                     |_|                   
""")

piedra = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

papel = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

tijera = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''
cont1 = 0
cont2 = 0
x = 3
while x > 0:

    x -=1
    eleccion = int(input("¿ Que vas a elegir"
                         """"
                 1.-Piedra
                 2.- Papel
                 3.- Tijera
                          """))
    comp_eleccion = random.randint(1, 3)

    if eleccion == 1:
        print(piedra)
        print("La computadora eligio: ")
        if comp_eleccion == 1:
            print(piedra)
            print(" Es un empate ")
        elif comp_eleccion == 2:
            print(papel)
            print("***** Haz perdido *****")
            cont2 +=1
        else:
            print(tijera)
            print("----->Haz ganado<-----")
            cont1+=1
    elif eleccion == 2:
        print(papel)
        print("La computadora eligio: ")
        if comp_eleccion == 1:
            print(piedra)
            print("---> Haz Ganado <----")
            cont1+=1
        elif comp_eleccion == 2:
            print(papel)
            print(" Es un empate ")
        else:
            print(tijera)
            print(" ***** Haz Perdido ")
            cont2+=1
    elif eleccion == 3:
        print(tijera)
        print(" La computadora eligió ")
        if comp_eleccion == 1:
            print(piedra)
            print(" **** Haz Perdido ****")
            cont2+=1
        elif comp_eleccion == 2:
            print(papel)
            print("-----> Haz ganado <-----")
            cont1+=1
        else:
            print(tijera)
            print(" Es un empate ")
    else:
        print("""Entrada invalida
                   debes elegir entre
                   1 a 3 respectivamente
                   Lee las instrucciones""")

else:
    print(" Se ha terminado el juego ")
    if cont1>cont2:
        print(f" *** El jugador ha ganado con * {cont1} * partidas ganadas")
    elif cont1==cont2:
        print(" Ha sido un empate ")
    else:
        print(f"La computadora ha ganado con * {cont2} * partidas ganadas")
