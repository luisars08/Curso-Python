def evaluarAlumno(nota):
    valoracion = "Desconocido"
    if nota < 5:
        valoracion = "Suspenso"
    else:
        valoracion="Aprobado"
    return valoracion

notaAlumno=int(input("Introduce la calificación del Alumno: "))
print( evaluarAlumno(notaAlumno) )