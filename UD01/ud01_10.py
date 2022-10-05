#10. Una empresa que gestiona un parque acuático te solicita
#  una aplicación que les ayude a
#calcular el importe que hay que cobrar en la taquilla 
# por la compra de una serie de entradas (cuyo
#número será introducido por el usuario). Existen dos tipos de entrada:
#  infantiles, que cuestan
#15,50 €; y de adultos, que cuestan 20 €.
#En el caso de que el importe total sea igual o superior a 100 €, 
# se aplicará automáticamente un
#bono descuento del 5%
MULTIPLODESCUENTO = 0.95
UMBRAL_DESCUENTO= 100
PRECIO_ENTRADA_INFANTIL = 15.50
PRECIO_ENTRADA_ADULTO = 20
tickinfantil = int(input("¿Cuantas entradas infantiles desea? "))
tickadulto = int(input("¿Cuantas entradas adulto desea? "))
preciobase = tickadulto * PRECIO_ENTRADA_ADULTO + tickinfantil * PRECIO_ENTRADA_INFANTIL
importeConDescuento = preciobase * MULTIPLODESCUENTO
abono = preciobase if preciobase < UMBRAL_DESCUENTO else importeConDescuento
print ("El precio a abonar es de:", round(abono,2), "€", sep = (" "))
print("Se ha aplicado un",int((1-MULTIPLODESCUENTO)*100),"por ciento de descuento") if abono == importeConDescuento else print("")

