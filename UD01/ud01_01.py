#. Un economista te ha encargado un programa para realizar 
# cálculos con el IVA. La aplicación debe solicitar la base 
# imponible y el IVA que se debe aplicar. Muestra en pantalla el 
# importe correspondiente al IVA y al total.
base_imponible =  float(input("Ingrese la base imponible: "))
iva = float(input("Ingrese el IVA: "))
iva_final = base_imponible * (iva / 100)
precio_final = iva_final + base_imponible
print("El iva total es", round(iva_final,2),"€",sep=" ")
print("El importe correspondiente es",round(precio_final,2) ,"€",sep= " ")