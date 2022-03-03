rd = float(input("alumnos de redes: "))
contabilidad = float(input("alumnos de contabilidad: "))
diseño = float(input("alumnos de diseño: "))


total = (rd + contabilidad + diseño)

print("porcentaje de alumnos de rd es: ", ((rd/total)*100))
print("porcentaje de alumnos de contabilidad es: ", ((contabilidad/total)*100))
print("porcentaje de alumnos de diseño es: ", ((diseño/total)*100))