#Lista de funciones utiles de Python

#Cadena al reves
cadena = "hola"
print(cadena[::-1]) #Devuelve 'aloh'

#Splitear cadena
cadena_split = "Hola mundo"
cadena_spliteada = cadena_split.split(" ")
print cadena_spliteada # Devuelve la lista ['Hola', 'mundo']


#Devuelve el numero de ocurrencias de un texto en otro
cadena = "hola"
print(cadena.count("o")) #Devuelve 1 porque ha encontrado solo 1 'o' en la cadena principal

#Ordenar una lista
lista = [2,0,56,4,33,21,58,6]
lista.sort()
print lista #Devuelve la lista ordenada -> [0, 2, 4, 6, 21, 33, 56, 58]

#eliminar elemento de lista
indice_a_eliminar = 2
lista.pop(indice_a_eliminar)
print lista #Devuelve la lista -> [0, 2, 6, 21, 33, 56, 58]


#DICCIONARIOS
asignaturas = {"Matematicas":0,"Fisica":0,"Quimica":0,"Historia":0,"Lengua":0}

#eliminar un objeto de un diccionario
del asignaturas["Matematicas"]
print asignaturas #Devuleve el mapa excepto la asignatura 'Matematicas', que ha sido eliminada