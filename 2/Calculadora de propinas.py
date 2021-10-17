print("Bienvenido a la calculadora de propinas")
total_factura = float(input("¿ Cuanto es el total de la cuenta ? $"))
propina = float(input("¿ Cual es el porcentaje que se debe dejar? % "))
personas = int(input("¿ Entre cuantas personas se divirá la cuenta ?"))

tot_propina = total_factura * (propina / 100)
final_factura = (total_factura + tot_propina)

tot_cadauno = final_factura / personas
round(tot_cadauno, 2)
print(f"Cada persona debe pagar: ${tot_cadauno}")