alumnonotaT1 = float (input("taller 1: "))
alumnonotaT2 = float (input("taller 2: "))
alumnonotaT3 = float (input("taller 3: "))


examen = float (input("examen nota: "))

proyectofinal = (input("proyecto: "))


notafinal = (alumnonotaT1 + alumnonotaT2 + alumnonotaT3)/3 *.50
examenalumno = examen * 0.30
proyecto = proyectofinal*0.20

notaalumno = notafinal + examenalumno + proyecto
print("La nota final del alumno es: ", notaalumno)