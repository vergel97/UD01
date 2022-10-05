n = int(input("Introduce el número entero n: "))
resto1 = n % 2
resto2 = n % 3
print(n,"Es multiplo de 2") if resto1 == 0 else print(n,"no es multiplo de 2")
print(n,"Es multiplo de 3") if resto2 == 0 else print(n,"no es multiplo de 3")