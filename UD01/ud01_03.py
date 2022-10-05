#03. Crea un programa que pida la base y la altura de un triángulo y muestre su área.

#Área Triángulo = (base * altura) / 2
base_triangulo = float(input("Introduzca el valor de la base del triangulo en cm: "))
altura_triangulo = float(input("Introduzca el valor de la altura del triangulo en cm: "))
area_triangulo = (base_triangulo * altura_triangulo)/2
print("El area de su triangulo es", area_triangulo, "cm", sep = (" "))