#Escribir un programa que almacene el diccionario con los creditos de las asignaturas de un curso {'Matematicas': 6, 'Fisica': 4, 'Quimica': 5} y despues muestre por pantalla los creditos de cada asignatura en el formato <asignatura> tiene <creditos> creditos,
# donde <asignatura> es cada una de las asignaturas del curso, y <creditos> son sus creditos. Al final debe mostrar tambien el numero total de creditos del curso.

diccionarioAsignaturas = {"Matematicas": 6 , "Fisica": 4, "Quimica": 7, "Fisolofia": 5, "Ingles": 4, "Historia": 8}
total_creditos = 0

for i in diccionarioAsignaturas.keys():
    print "La asignatura "+i+" tiene "+str(diccionarioAsignaturas.get(i))+" creditos"
    total_creditos += diccionarioAsignaturas.get(i)

print "Total creditos curso "+str(total_creditos)
