a = int(input ("Introduce el número entero a: "))
resto=  (a % 10) 
print(resto,"es par", sep=(" ")) if resto % 2 == 0 else print(resto," no es par",sep=(" "))