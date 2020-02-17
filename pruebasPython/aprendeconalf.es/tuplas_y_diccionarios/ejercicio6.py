#Escribir un programa que almacene las asignaturas de un curso (por ejemplo Matematicas, Fisica, Quimica, Historia y Lengua) en una lista, pregunte al usuario la nota que ha sacado en cada asignatura y elimine de la lista las asignaturas aprobadas. Al final el programa debe mostrar por pantalla las asignaturas que el usuario tiene que repetir.

asignaturas = {"Matematicas":0,"Fisica":0,"Quimica":0,"Historia":0,"Lengua":0}

for i in asignaturas.keys():
    nota = int(input("Que nota has sacado en "+i+": "))
    if nota < 5:
        del asignaturas[i]
    else:
        asignaturas[i] = nota

print "ASIGNATURAS APROBADAS: "+str(asignaturas)