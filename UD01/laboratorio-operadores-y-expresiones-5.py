
hour = int(input("Hora de inicio (horas): "))
mins = int(input("Minuto de inicio (minutos): "))
dura = int(input("Duración del evento (minutos): "))
minutos= (mins + dura) % 60
houras = int(hour+(mins+dura)/60)%24
print(houras,":",minutos,sep="")

#El simbolo de porcentaje nos sirve para extraer el resto de una division,
#lo utilizamos para no pasarnos de 24h ni de 60 minutos.
