#12. Imagina que acabas de abrir una nueva cuenta de ahorros 
# que te ofrece el 4% de interés al año. Estos ahorros debido 
# a intereses, que no se cobran hasta finales de año, se te añaden
#  al balance final de tu cuenta de ahorros. Escribir un programa que
#  comience leyendo la cantidad de dinero depositada en la cuenta de
#  ahorros, introducida por el usuario. Después el programa debe
#  calcular y mostrar por pantalla la cantidad de ahorros tras 
# el primer, segundo y tercer años. Redondear cada cantidad a dos
#  decimales.

INTERES_AÑO_PORCENTAJE = 1.04

deposito = float(input("Introduce la cantidad de dinero que ingresaste en euros: "))

ahorroPrimerAño = deposito * INTERES_AÑO_PORCENTAJE
ahorroSegundoAño = ahorroPrimerAño * INTERES_AÑO_PORCENTAJE 
ahorroTercerAño =  ahorroSegundoAño * INTERES_AÑO_PORCENTAJE

print ("El primer año tendras: ", round (ahorroPrimerAño,2), "€", end=(". "))
print ("El segundo año tendras: ", round (ahorroSegundoAño,2), "€", end=(". "))
print ("El Tercer año tendras: ", round(ahorroTercerAño,2), "€")