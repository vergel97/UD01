a = int(input ("Introduce el número entero de tres cifras a: "))
algoritmo3 =  (a % 10) 
algoritmo2 =(a//10) %10
algoritmo1 = (a//100)
print(algoritmo1 , "es par.", sep = (" ")) if algoritmo1 % 2 ==0 else print(algoritmo1,"no es par", sep = (" "))