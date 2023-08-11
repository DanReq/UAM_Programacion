#Daniel Reséndiz Quiroz - 2183034962

#Calificación de alumnos

#Ingreso de número de asignaturas
def calificaPromedio(asignatura):
    #asignatura = int(input())
    suma = 0
    for i in range(asignatura):
        calificacion = int(input())
        suma = suma + calificacion

    #Calculo de promedio
    promedio = suma / asignatura

    #Asignación de letra
    if promedio >= 90:
        calif = 'A'
    elif promedio >= 80 and promedio < 90:
        calif = 'B'
    elif promedio >= 70 and promedio < 80:
        calif = 'C'
    elif promedio >= 60 and promedio < 70:
        calif = 'D'
    elif promedio < 60:
        calif = 'F'

    print(promedio)
    print(calif)