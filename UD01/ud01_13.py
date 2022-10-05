#13. Escribir una variante del progama anterior que pregunte al usuario una cantidad a invertir,
#  el interés anual y el número de años, y muestre por pantalla el capital obtenido en la inversión.


deposito = float(input("Introduce la cantidad de dinero que ingresaste en euros: "))
interesAnual = float (input("Introduce el tipo de interés anual en tanto porciento: "))
numAños = int (input("Introduce el número de años que pretendes mantener el deposito: "))


ahorro = deposito * (1 + interesAnual /100 ) ** numAños

print("Tu dinero total es: ",round(ahorro,2), "€")
