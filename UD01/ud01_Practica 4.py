#Realiza un programa que realice simulaciones de la factura de electricidad como 
# la de la figura con los siguientes ajustes:

#El usuario introducirá los siguientes datos de entrada:
#Potencia Punta
#Potencia Valle
#Consumo Punta
#Consumo Llano
#Consumo Valle
#Número de días

#El programa mostrará una tabla resumen como la de la siguiente figura:



#El importe de los distintos conceptos anteriores y del total de la factura se calculará  
# usando las fórmulas que se muestran en el siguiente detalle, implementando los valores resaltados
#  en amarillo como constantes al inicio del código:

#Nota: La potencia utilizada en el cálculo del Margen de comercialización, en el apartado de
#  Término Fijo, corresponde a la Potencia Punta.
#Nota2: El cálculo del importe del alquiler del Equipo de medida, que se valora en 0,81€/mes, 
# resulta más exacto si antes se calcula el valor anual del alquiler, es decir, multiplicando
#  0,81 * 12 meses, y lulego utilizando el número de días del año (365) en el cálculo final. 
# Ejemplo:

#ImporteAlquilerEquipoMedida = NumDíasFacturados * (0,81 * 12 / 365)
PRECIOKWAÑOPUNTA = 30.67266
PRECIOKWAÑOVALLE = 1.424359 
MARGENPRECIOCOMERCIALIZACION =  3.113 
#Estas 3 varriables son necesarias para el calulo de Pvalle ,Ppunto y margendecomerzialización
AÑO= 365
VARIABLEPUNTATERMINOVARIABLE = 0.133118
VARIABLEVALLETERMINOVARIABLE = 0.006001
VARIABLELLANOTERMINOVARIABLE =  0.041772
#Estas 3 variables las utilizamos para el calculo de Termino Variable
VARIABLECOSTEENERGIA = 0.1321
#VARIABLE COSTE ENERGIA
VARIABLEIMPUESTOELECTRICO = 0.0511269632
ALQUILERCONTADORMES = 0.80
MES = 31
BASEIVA= 0.10

potenciaPunta = float(input("Introduce la potencia punta en Kw: "))
potenciaValle = float (input("Introduce la potencia valle en Kw: "))
consumoPunta = float (input("Introduce el consumo punta en Kwh: "))
consumoValle = float (input("Introduce el consumo valle en Kwh: "))
consumoLlano = float(input("Introduce el consumo llano en kwh: "))
consumo = float(input("Indique su consumo en Kwh: "))
numDias = int (input("Introduce el número de días de facturación: "))


#Terminofijo
pvalle = potenciaValle * PRECIOKWAÑOVALLE * numDias/AÑO
ppunta = potenciaPunta * PRECIOKWAÑOPUNTA * numDias/AÑO
margenDeComercializacion = potenciaPunta * MARGENPRECIOCOMERCIALIZACION * numDias /AÑO
terminoFijo = round(pvalle,2) +round (ppunta,2) + round(margenDeComercializacion,2)
#TerminoVariable
pvalle2 = consumoValle * VARIABLEVALLETERMINOVARIABLE
pPunta2 = consumoPunta * VARIABLEPUNTATERMINOVARIABLE
pLlano = consumoLlano * VARIABLELLANOTERMINOVARIABLE
costeEnergía = consumo * VARIABLECOSTEENERGIA
terminoVariable = costeEnergía + pvalle2 + pLlano +pPunta2
#impuestoElectrico
impuestElectrico = (terminoVariable+terminoFijo) * VARIABLEIMPUESTOELECTRICO
#equipodemedida
equipoMedida = ALQUILERCONTADORMES * (numDias/MES)
#IVA
sinImpuestos = terminoFijo + terminoVariable + impuestElectrico + equipoMedida
iva = sinImpuestos * BASEIVA
#TOTAL
totalFactura = sinImpuestos + iva

print("Su facturación")
print ("Termino fijo:   ",round(terminoFijo,2)," €")
print ("Termino llano:   ",round (terminoVariable,2)," €")
print("Impuesto eléctrico:   ",round(impuestElectrico,2),"€")
print("alquiler contadores:   ",round(equipoMedida,2)," €")
print("IVA:   ",round(iva , 2), " €")
print("TOTAL FACTURA   ", round( totalFactura, 2), " €")
print(round(terminoFijo,), "+",round( terminoVariable,2),"+",round(impuestElectrico,2), "+", round(equipoMedida,2),"+", round(iva,2) , sep=(" "))