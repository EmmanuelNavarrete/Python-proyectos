#Programa que diga si haz aprobado o no
calificacion1 = int(input("¿ Cual es tu primer calificacion ? "))
calificacion2 = int(input("¿ Cual es tu segunda calificacion ? "))
calificacion3 = int(input("¿ Cual es tu tercer calificacion ? "))

cal_fin= (calificacion1 + calificacion2 + calificacion3) / 3
if cal_fin >= 70:
    print("Haz aprobado con una calificacion de: " + str(cal_fin))
else:
    print("Haz reprobado,  la calificacion final es de: " + str(cal_fin))
