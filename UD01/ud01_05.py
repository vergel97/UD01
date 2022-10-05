#02. Escribe un programa que tome como entrada un número entero e indique qué  
# cantidad hay que sumarle para que el resultado sea múltiplo de 7. Un ejemplo:

#A 2 hay que sumarle 5 para que el resultado (2+5=7) sea múltiplo de 7.
#A 13 hay que sumarle 1 para que el resultado (13+1=14) sea múltiplo de 7.

#Si proporcionas el número 2 o el 13, la salida de la aplicación debe ser 5 o 1, respectivamente.

#Pista: El operador módulo puede ser muy útil para solucionar esta actividad.
numero_multiplo = int(input("Introduzca un numero: "))
numero_divisor =  int(input("Introuce el valor del divisor: "))
a = numero_multiplo //numero_divisor
numero_suma = (a+1)*numero_divisor - numero_multiplo
print("El valor que debe sumarle a", numero_multiplo,"es igual a",numero_suma, sep=" ")
#es este caso no me hizo falta el operador módulo
resto = numero_multiplo % numero_divisor
resto2 = 0 if resto == 0 else numero_divisor - resto
print("El valor que debe sumarle a", numero_multiplo,"es igual a",resto2, sep=" ")
#operador ternario es parecido al if value_if if condition else value_else