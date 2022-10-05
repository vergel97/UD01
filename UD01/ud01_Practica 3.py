#Dada la siguiente receta de compota de manzana, u otra similar que encuentres en Internet, 
# realiza un programa que haga lo siguiente:
#Mostrar un nombre o título adecuado en pantalla:
#Mostrar la URL de la receta elegida:
#Mostrar el número de personas y las cantidades necesarias de manzana, agua, azúcar y limón 
# para las que está pensada la receta elegida.
#Opcionalmente puedes mostrar los otros ingredientes en otra línea de salida.
#Solicitar por teclado al usuario un número de personas para el cual adaptar la receta.
#Mostrar por pantalla las cantidades de manzana, agua, azúcar y limón necesarias para elaborar 
# la receta para el número de personas introducido. 

#Como extra, basándote en los precios de los ingredientes principales (manzanas y azúcar) de 
# un supermercado a tu elección, indica el coste de cada uno de los ingredientes de la receta 
# a elaborar y la suma total en euros, con hasta 2 decimales.

#Opcionalmente puedes mostrar una recomendación de reducir al máximo la cantidad de azúcar para 
# que la receta sea más saludable.
TITULODERECETA = "RECETA DE COMPOTA DE MANZANA"
URLRECETA = "https://www.recetasderechupete.com/compota-de-manzana-casera/12509/"
KILOSMANZANASNECESARIAS = 1.5
MLAGUA = 330
CUCHARADADELIMON = 1
NUMPERSONASRECETAS = 6
GRAMOSAZUCAR = 120
PRECIOMANZANASEUROSKG = 1.59
PRECIOAZUCAREUROSKG = 0.99
GRAMOSAKG = 1000

print(TITULODERECETA)
print("Para saber más sobre esta receta: ", URLRECETA)
print("La receta esta pensada para", NUMPERSONASRECETAS, "personas", end=("."))
print( " Se necesitan",KILOSMANZANASNECESARIAS, "kilos de manza",MLAGUA, "ml de agua", GRAMOSAZUCAR, "gramos de azucar Y", CUCHARADADELIMON, "de limón", sep = (" ") )

numPersonas = int(input("Cuantas personas van a comer: " ))

mlAguanecesaria = MLAGUA / NUMPERSONASRECETAS * numPersonas
limonnecesaria = CUCHARADADELIMON / NUMPERSONASRECETAS * numPersonas
kgManzanasNecesarias = KILOSMANZANASNECESARIAS / NUMPERSONASRECETAS * numPersonas
gAzucarNecesario = GRAMOSAZUCAR / NUMPERSONASRECETAS * numPersonas
costemanzanas = kgManzanasNecesarias * PRECIOMANZANASEUROSKG
costeazucar = gAzucarNecesario / GRAMOSAKG if gAzucarNecesario % GRAMOSAKG == 0 else gAzucarNecesario / GRAMOSAKG + 1
costetotal = costemanzanas + costeazucar

print (" Vas a necesitar",round(kgManzanasNecesarias,2), "kilos de manza",round(mlAguanecesaria,2), "ml de agua", round(gAzucarNecesario,2), "gramos de azucar Y", int(limonnecesaria), "limón", sep = (" ")) if limonnecesaria <=1 else print (" Vas a necesitar",round(kgManzanasNecesarias,2), "kilos de manza",round(mlAguanecesaria,2), "ml de agua", round(gAzucarNecesario,2), "gramos de azucar Y", int(limonnecesaria), "limónes", sep = (" "))
print ( "El coste total de las manzanas sería", round(costemanzanas,2),"Euros .El coste total del azucar sería", round(costeazucar,2), "euros.", sep=(" "))
print ("El coste total son:", round(costetotal,2), sep =(" "))
print("RECUERDA: EL ALTO CONSUMO DE AZUCAR NO ES SALUDABLE ¡REDUCELO!")