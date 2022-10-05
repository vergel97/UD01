#08. Diseña una aplicación que solicite al usuario 
# que introduzca una cantidad de segundos
#La aplicación debe mostrar cuántas horas, minutos y segundos 
# hay en el número de segundos
#introducidos por el usuario.
segundos = int(input("Introduce una cantidad de segundos: "))
horas = segundos // 3600
minutos = segundos % 3600 // 60
segundos = segundos % 60
print( horas ,"h",minutos,"min" , segundos, "s" , sep = (" "))