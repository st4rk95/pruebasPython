#Escribir un programa que permita gestionar la base de datos de clientes de una empresa. Los clientes se guardaran en un diccionario en el que la clave de cada cliente sera su NIF, y el valor sera otro diccionario con los datos del cliente
# (nombre, direccion, telefono, correo, preferente), donde preferente tendra el valor True si se trata de un cliente preferente. El programa debe preguntar al usuario por una opcion del siguiente menu:
# (1) Annadir cliente, (2) Eliminar cliente, (3) Mostrar cliente, (4) Listar todos los clientes, (5) Listar clientes preferentes, (6) Terminar. En funcion de la opcion elegida el programa tendra que hacer lo siguiente:

#Preguntar los datos del cliente, crear un diccionario con los datos y annadirlo a la base de datos.
#Preguntar por el NIF del cliente y eliminar sus datos de la base de datos.
#Preguntar por el NIF del cliente y mostrar sus datos.
#Mostrar lista de todos los clientes de la base datos con su NIF y nombre.
#Mostrar la lista de clientes preferentes de la base de datos con su NIF y nombre.
#Terminar el programa.


def annadir_cliente():
    print 1


def eliminar_cliente():
    print 2


def mostrar_cliente():
    print 3


def listar_clientes():
    print 4

cerrar_programa = False