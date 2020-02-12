#Escribir un programa que almacene las asignaturas de un curso (por ejemplo Matematicas, Fisica, Quimica, Historia y Lengua) en una lista, pregunte al usuario la nota que ha sacado en cada asignatura, y despues las muestre por pantalla con el mensaje En <asignatura> has sacado <nota> donde <asignatura> es cada una des las asignaturas de la lista y <nota> cada una de las correspondientes notas introducidas por el usuario

asignaturas = {"Matematicas":0,"Fisica":0,"Quimica":0,"Historia":0,"Lengua":0}

for i in asignaturas.keys():
    nota = int(input("Que nota has sacado en "+i+": "))
    asignaturas[i] = nota

for i in asignaturas.keys():
    print "En "+i+" has sacado un "+str(asignaturas.get(i))
