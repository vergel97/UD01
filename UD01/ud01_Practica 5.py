
print("Evaluador de notas")
print(sep="/n")
print(sep="/n")
#funciona
print("El programa funciona? ")
print("1.Si y funciona")
print("2. Si pero no hace lo que debe")
print("3. no")
opcion1 = int(input("Elige 1 ,2 o 3 "))
print(sep="/n")

#eficiencia
print("El programa es eficiente?")
print("1. Sí")
print("2. Regular")
print("3. No")
opcion2 = int(input("Elige 1 ,2 o 3 "))
print(sep=("n/"))

#Estruturas u tipos de datos
print("Usa estructuras y tipos de datos adecuados al problema?")
print("1. Siempre")
print("2. A veces")
print("3. Nunca")
opcion3 = int(input("Elige 1 ,2 o 3 "))
print(sep=("n/"))

#Identificadores Adecuados
print("Usa identificadores adecuados?")
print("1. Siempre")
print("2. A veces")
print("3. Nunca")
opcion4 = int(input("Elige 1 ,2 o 3 "))
print(sep=("n/"))

#legibilidad
print("El programa es legible?")
print("1. Mucho")
print("2. Regular")
print("3. Poco")
opcion5 = int(input("Elige 1 ,2 o 3 "))
print(sep=("n/"))

#información completa al usuario
print("Presenta la información completa al usuario?")
print("1. Sí")
print("2. Regular")
print("3. No")
opcion6 = int(input("Elige 1 ,2 o 3 "))
print(sep=("n/"))

#Entrega correcta
print("La entrega se ha realizado correctamente?")
print("1. Sí")#print("2. Error formato")
print("3. Falta la entrega")
opcion7 = int(input("Elige 1 ,2 o 3 "))
print(sep=("n/"))


puntFunciona = 4 if opcion1 == 1 else 0
puntFunciona = 2 if opcion1 == 2 else puntFunciona

puntEficiente = 1 if opcion2 == 1 else 0
puntEficiente = 0.5 if opcion2 == 2 else puntEficiente

puntEstructuras = 1 if opcion3 == 1 else 0
puntEstructuras = 0.5 if opcion3 == 2 else puntEstructuras

puntIdentificadores =1.5 if opcion4 == 1 else 0
puntIdentificadores = 0.75 if opcion4 == 2 else puntIdentificadores

puntLegibilidad =1.5 if opcion5 == 1 else 0
puntLegibilidad = 0.75 if opcion5 == 2 else puntLegibilidad

puntInformacion = 1 if opcion6 == 1 else 0
puntInformacion = 0.5 if opcion6 == 2 else puntInformacion

puntFinal = puntFunciona + puntEficiente + puntEstructuras + puntIdentificadores + puntInformacion + puntLegibilidad

#La entrega correcta hay que calcularla despues de la puntfinal ya que puede varias esta misma a 0
notaFinal = puntFinal -1 if opcion7 == 2 else puntFinal
notaFinal = 0  if opcion7 == 3 else notaFinal 
 
print("La nota final del Alumno es ",notaFinal)
