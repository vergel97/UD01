#09. Solicita al usuario tres distancias:
#• La primera, medida en milímetros.
#• La segunda, medida en centímetros.
#• La última, medida en metros.
#Diseña un programa que muestre la suma de las tres longitudes introducidas expresada en
#centimetros
mm = float(input("Introduce una media en milímetros: "))
cm = float(input("Introduce una medida en centimetros: "))
m = float(input("Introduce una medida en metros: "))
cmtotal = mm / 10 + cm + m *100
print("La suma de sus medidas introducidas en cm es", round(cmtotal,2))