a = int(input ("Introduce el número entero de tres cifras a: "))
algoritmo3 =  (a % 10) 
algoritmo2 =(a//10) %10
algoritmo1 = (a//100)
algoritmofinal = algoritmo1 + algoritmo2 + algoritmo3
print("La suma de los dígitos de",a,"es",algoritmofinal, sep =(" "))