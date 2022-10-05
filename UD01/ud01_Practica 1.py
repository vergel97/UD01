#A partir del nombre y horas de un módulo de FP, por ejemplo, “Programación”, 240 horas. 
# No es necesario pedir estos datos por teclado. Codifícalos como constantes en tu programa 
# y utiliza el tipo de dato String para almacenar el nombre del módulo.

#Calcula y muestra por pantalla:
#nº de sesiones de 50’.
#número de faltas sin justificar que implican un apercibimiento (>6%)
#número de faltas sin justificar para pérdida de evaluación continua (>10%)

#Solicita por teclado un número de faltas de un alumno concreto e indica si implica
#  apercibimiento, pérdida de evaluación continua o ningún problema.

#¿Cuántas líneas de código tendrías que modificar en tu programa para que muestre los datos relativos a otro módulo de FP? Por ejemplo:
#“Linguaxes de marcas e sistemas de xestión de información”, 133 horas
#“Bases de Datos”, 187 horas
HORAS = 240
ASIGNATURA = "programación"
PORCENTAJEAPERCIBIMIENTO = 0.06
PORCENTAJEAPERDIDA = 0.10
MINUTOSSESION = 50

minutosTotalAsignatura = 240*60
sesiones50Min = minutosTotalAsignatura/ MINUTOSSESION
horasApercibimiento = sesiones50Min * PORCENTAJEAPERCIBIMIENTO
horasPerdidaEvaluación = sesiones50Min * PORCENTAJEAPERDIDA
faltasAlumno = int(input("Introduce las faltas del alumno: "))
apercibir = faltasAlumno > horasApercibimiento
perdidaEvaluacion = faltasAlumno > horasPerdidaEvaluación
print("Las sesiones de",ASIGNATURA,"son",int (sesiones50Min), "sesiones", sep=(" ") )
print("Las faltas maximas antes de apercibir a un alumno en", ASIGNATURA, "son", int(horasApercibimiento),"faltas", sep=(" "))
print("Las faltas maximas antes de perder la evaluación continua en ", ASIGNATURA, "son", int(horasPerdidaEvaluación),"faltas", sep=(" "))
print(faltasAlumno,"faltas implica percibir al alumno ", sep=(" ")) if  apercibir == True else print("El alumno no esta apercibido")

print(faltasAlumno,"faltas implica perder la evalucación continua", sep=(" ")) if perdidaEvaluacion == True  else print("El alumno no pierde la evaluación continua")
