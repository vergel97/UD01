#Realiza un programa que facilite el trabajo de estos periodistas 
# que acepte por teclado un número de hectáreas e imprima a cuántos campos de fútbol
#  equivale.

#Para evitar discriminaciones a aficionados de otros deportes y para 
# que también puedan entender la magnitud de la tragedia, calcula e imprime el valor de 
# superficie introducido en número de campos de baloncesto, de tenis, etc. Para residentes
#  en Madrid (o no) puedes ofrecer también el dato en número equivalente de parques del Retiro 
# quemados.

#Puedes personalizar el programa con alguna medida equivalente de tu localidad o región de origen.

#Para los cálculos puedes usar las siguientes dimensiones:
#1 hectárea = 100 x 100 metros = 10000 m2
#Campo de fútbol según la FIFA (media): 105 x 70 metros 
#Cancha de baloncesto: 28 x 15 metros
#Pista de tenis (dobles): 23,77 x 10,97 metros
#Parque del Retiro: 125 hectáreas
CONVERSIONHECTAREAMETRO = 10000
AREACAMPOFUTBOL = 105*70
AREACANCHADEBALONCESTO = 28 * 15
AREATENIS = 23.77 * 10.97
HECTAREASPARQUERETIRO = 125

numeroHectareas = float(input("Introduce el número de Hectareas quemadas: "))
camposQuemados = numeroHectareas / (AREACAMPOFUTBOL/CONVERSIONHECTAREAMETRO)
canchaQuemadas = numeroHectareas / (AREACANCHADEBALONCESTO/CONVERSIONHECTAREAMETRO)
tenisquemado = numeroHectareas / (AREATENIS/CONVERSIONHECTAREAMETRO)
retirosquemados = numeroHectareas / HECTAREASPARQUERETIRO

print("El total de campos de futbol quemados son", int (camposQuemados), sep=(" "))
print("El total de canchas de baloncesto quemadas son", int (canchaQuemadas), sep=(" "))
print("El total de pistas de tenis quemadas son", int (tenisquemado), sep=(" "))
print("El total de parques del retiro quemados son", int (retirosquemados), sep=(" "))