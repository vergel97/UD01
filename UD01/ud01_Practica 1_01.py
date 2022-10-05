import string


HORASPROGRAMACION = 240
HORASLENGUAJEDEMARCAS = 133
HORASBASEDEDATOS = 187
PORCENTAJEAPERCIBIMIENTO = 0.06
PORCENTAJEAPERDIDA = 0.10

asignatura = str (input("Introduce el nombre de la asignatura en minusculas y sin acentos: "))
minutosTotalAsignatura = 240*60 if asignatura == "programacion" else print()
minutosTotalAsignatura = 240*60 if asignatura == "lenguaje de marcas y sistemas de gestion e informacion" else print()
minutosTotalAsignatura = 240*60 if asignatura == "base de datos" else print()
sesiones50Min = minutosTotalAsignatura/50
horasApercibimiento = sesiones50Min * PORCENTAJEAPERCIBIMIENTO
horasPerdidaEvaluación = sesiones50Min * PORCENTAJEAPERDIDA
faltasAlumno = int(input("Introduce las faltas del alumno: "))

print("Las sesiones de",asignatura,"son",int (sesiones50Min), "sesiones", sep=(" ") )
print("Las faltas para apercibir a un alumno en", asignatura, "son", int(horasApercibimiento),"faltas", sep=(" "))
print("Las faltas para perder la evaluación continua en ", asignatura, "son", int(horasPerdidaEvaluación),"faltas", sep=(" "))
print(faltasAlumno,"implica percibir al alumno ", sep=(" ")) if faltasAlumno >= horasApercibimiento  else print("El alumno no esta apercibido")
print(faltasAlumno,"implica perder la evalucación continua", sep=(" ")) if faltasAlumno >= horasPerdidaEvaluación  else print("El alumno no pierde la evaluación continua")