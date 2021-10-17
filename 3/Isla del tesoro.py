print('''
                                                        
        =***=@*==--========++++**+***####*+       
      :%=: --%*+++=+++++============%@**#*:       
      %= - -%+#.:::.:::..:::.:::.:-%%.-#=#        
     -%:: -*##:              .....*@::=@=+        
     ++  :+@+%::::.::::.::.....   @#:-%%*.        
     **::-*##-                   .@*:-%+#         
     =#.:.%+%::.:.:.::::::::::::::%#-:@*=         
      %+ =*#=          ....:::::--#@**@*.         
      :%+%=%#****################***++=#          
       :%@*****#*###*#*****#+==*+==+=+***.        
        **%*%*--=+Encuentra el tesoro+=+*=:-+**-       
        #-:#==--==:+++--+=--===-=---+-+---++      
        %-.:#==--++***+=+*++*##**=++*+****#+#     
        @ ::-#============++-+-=---:::::::..%     
       .%  .=*            =.=# -     ......:#     
       -*:. -*:::::::::::::+===:::::...... :*     
       -* .:==                             -+     
        *+  *+:::::::::::::::::::::::::.::.==     
         ++ +-                             =-     
          =**:                             +:     
           =@*******************************.     
        
''')
print("Bienvenido a la isla del Tesoro.\n")
print("Para regresar a casa sano y salvo debes completar una mision")
print("Tu misión debes encontrar un tesoro\n")
print("¿Estas Listo?\n COMENCEMOS\n")
print("""
Bajas de tu barco y te adentras a la isla,
Sigues el camino principal y te encuentras con
dos desviaciones debes elegir una de las dos\n
""")
escoge_camino = input("Escoge izquierda o derecha ->>>>>?".lower())
if escoge_camino == "izquierda":
    print("Estas a salvo. CONTINUA!!!!\n")
    print("""
    Avanzando te encuentras con un rio.
    Tienes dos opciones para cruzar el rio.\n
    """)
    escoge_rio = input("Puedes -Nadar- o -esperar- un bote ->>>>>".lower())
    if escoge_rio == "esperar":
        print("Aveces la espera es la mejor opcion. ESTAS A SALVO!!\n")
        print("Despues de cruzar el rio, ahora estás en el nivel siguiente")
        print("Logras observar 3 puertas, Una verde, una blanca y una roja"
              "Debes pasar por alguna para llegar al tesoro\n")
        escoge_puerta = input("¿ Que puerta eligiras verde, blanca o roja? ->>>>>".lower())
        if escoge_puerta == "roja":
            print("FELICIDADES ERES ACREDOR A RECLAMAR TODO EL ORO DEL COFRE")
            print("""
                         ────────────────────██████──────────
             ──────────────────██▓▓▓▓▓▓██────────
             ────────────────██▓▓▓▓▒▒▒▒██────────
             ────────────────██▓▓▒▒▒▒▒▒██────────
             ──────────────██▓▓▓▓▒▒▒▒██──────────
             ──────────────██▓▓▒▒▒▒▒▒██──────────
             ────────────██▓▓▓▓▒▒▒▒▒▒██──────────
             ────────────████▒▒████▒▒██──────────
             ────────────██▓▓▒▒▒▒▒▒▒▒██──────────
             ──────────██────▒▒────▒▒██──────────
             ──────────████──▒▒██──▒▒██──────────
             ──────────██────▒▒────▒▒██──────────
             ──────────██▒▒▒▒▒▒▒▒▒▒▒▒██──────────
             ──────────████████████▒▒▒▒██────────
             ────────██▓▓▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒██──────
             ──────██▓▓▓▓▒▒▒▒▒▒▒▒▒▒▒▒▒▒▓▓▒▒██────
             ────██▓▓▓▓▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▓▓▒▒▒▒██──
             ──██▓▓▓▓▓▓▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▓▓▒▒▒▒██
             ██▓▓▒▒▓▓▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▓▓▒▒▒▒██
             ██▓▓▒▒▓▓▒▒▒▒▒▒▓▓▓▓▒▒▒▒▒▒▒▒▒▒▓▓▓▓▒▒██
             ██▓▓▓▓▓▓▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▓▓▓▓██
             ──████▐▌▓▓▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▐▌▐▌████──
             ────██▐▌▐▌▌▌▌▌▌▌▌▌▐▌▐▌▐▌▐▌▌▌▐▌██────
             ────██▌▌▐▌▐▌▌▌▐▌▌▌▌▌▐▌▌▌▌▌▌▌▌▌██────
             ──────██▌▌▐▌▐▌▐▌▐▌▐▌▐▌▐▌▌▌▌▌██──────
             ──────██▐▌▐▌▐▌████████▐▌▌▌▌▌██──────
             ────────██▒▒██────────██▒▒██────────
             ────────██████────────██████────────
                         """)
        elif escoge_puerta == "blanco":
            print("Lo siento escogiste la puerta equivocada y te mató jackie chan de un madrazo")
        elif escoge_puerta == "verde":
            print("Lo siento escogiste la puerta equivocada \n Memo aponte de mando a sus enanos a matarte")

        else:
            print("Hiciste una mala eleccion!!  ¡¡¡¡JUEGO TERMINADO!!!")
    elif escoge_rio == "nadar":
        print("HAZ SIDO DEBORADO POR COCODRILOS FIN DEL JUEGO")
    else:
        print("Haz escogido una respuesta erronea FIN")

elif escoge_camino == "derecha":
    print("OOPS Haz caido en un abujero")
else:
    print("MALA RESPUESTA FIN")
