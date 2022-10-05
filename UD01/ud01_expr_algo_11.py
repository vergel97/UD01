a = int(input ("Introduce el número entero de cuatro cifras a: "))
a = int(input ("El número introducido tiene menos de 4 cifras. Introduce el número entero de cuatro cifras a: ")) if a < 1000 else ()
a = int(input ("El número introducido tiene más de 4 cifras. Introduce el número entero de cuatro cifras a: ")) if a >9999 else ()
algoritmo1= a//1000
print(algoritmo1 , "es par.", sep = (" ")) if algoritmo1 % 2 ==0 else print(algoritmo1,"no es par", sep = (" "))