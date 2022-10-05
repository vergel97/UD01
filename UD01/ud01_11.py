print("Conversión de Temperaturas")
print("1. Celsius a Farenheit")
print("2. Farenheit a Celsius")
opcion = input ("Opcion? ")
temp = float(input("Temperatura: "))

tempFinal = temp * 9 / 5 + 32  if  opcion == 1  else (temp-32) *5/9
print (round(temp,4)," Celsius son", round(tempFinal,4), "farenheit") if opcion == 1 else print (round(temp,4)," farenheit son", round(tempFinal,4), "Celsius")