#06. Realiza un programa que solicite por teclado 
# la siguiente información relativa a un viaje 
# compartido en coche:
#- Distancia del trayecto recorrido (km)
#- Consumo medio del vehículo (litros por cada 100 km)
#- Precio aprox. combustible (€ por litro)
#- Número de pasajeros, incluyendo el conductor/a

#El programa deberá calcular y mostrar por pantalla la siguiente 
# información: 
#- Importe total estimado del trayecto.
#- Importe medio por km recorrido.
#- Importe a aportar por cada pasajero para compartir los gastos del viaje.



distancia_trayecto_km = float(input("Introduce la distancia del trayecto en km: "))
consumo_medio = float (input("Introduce el consumo medio en litros del vehículo cada 100 km: "))
precio_combustible = float(input("Introduce el precio del combustible aproximadamente en €: "))
num_pas = int(input("Introduce el número de pasajeros incluido el conductor: "))
#proceso
precio_total = precio_combustible * (consumo_medio/100)*distancia_trayecto_km
print("El precio total del trayecto son:", round (precio_total,2),"€", sep=(" "))
imp_med_km = precio_total/ distancia_trayecto_km
print("El importe medio por Km es:",round(imp_med_km,2),"€/km",sep=(" "))
precio_pasajero = precio_total/num_pas
print("El importe por pasajero es:",round(precio_pasajero,2),"€", sep = (" "))
litrosconsumidos = distancia_trayecto_km /100 *consumo_medio
print("Los litros consumidos son", litrosconsumidos, sep=(" "))