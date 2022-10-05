#Escribe un programa que lea por teclado la velocidad máxima de una carretera y 
# la velocidad de un coche que circula por ella en km/h. 
#El programa deberá imprimir True si la velocidad es adecuada y False en caso contrario, 
# teninendo en cuenta que no se debe circular por una carretera a menos de la mitad de 
# la velocidad máxima.
vmax = float(input("Introduce la velocidad máxima de la carretera en km/h : "))
vcoche = float (input("Introduce la velocidad del coche en km/h : "))
resultado =  vmax >= vcoche and vcoche > vmax/2
print(resultado)
