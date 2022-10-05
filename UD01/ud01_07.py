#07. Dado el siguiente polinomio de segundo grado:
#y = ax2 + bx + c
#crea un programa que pida los coeficientes a, b y c, así como el valor de x, y que calcule el valor
#correspondiente de y.
a = float(input("Introduce el valor de a para el polinomio ax2 + bx + c: "))
b = float(input("Introduce el valor de b para el polinomio ax2 + bx + c: "))
c = float(input("Introduce el valor de c para el polinomio ax2 + bx + c: "))
x= float (input("Introduce el valor de x para el polinomio ax2 + bx + c: "))
y = a * x ** 2 + b * x + c
print("El valor de \"y\" es: ",round(y,2))