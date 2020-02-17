#Escribir un programa que permita gestionar la base de datos de clientes de una empresa. Los clientes se guardaran en un diccionario en el que la clave de cada cliente sera su NIF, y el valor sera otro diccionario con los datos del cliente
# (nombre, direccion, telefono, correo, preferente), donde preferente tendra el valor True si se trata de un cliente preferente. El programa debe preguntar al usuario por una opcion del siguiente menu:
# (1) Annadir cliente, (2) Eliminar cliente, (3) Mostrar cliente, (4) Listar todos los clientes, (5) Listar clientes preferentes, (6) Terminar. En funcion de la opcion elegida el programa tendra que hacer lo siguiente:

#Preguntar los datos del cliente, crear un diccionario con los datos y annadirlo a la base de datos.
#Preguntar por el NIF del cliente y eliminar sus datos de la base de datos.
#Preguntar por el NIF del cliente y mostrar sus datos.
#Mostrar lista de todos los clientes de la base datos con su NIF y nombre.
#Mostrar la lista de clientes preferentes de la base de datos con su NIF y nombre.
#Terminar el programa.

#Se annade la opcion de poder editar los datos de un cliente
diccionario_clientes = {}

def annadir_cliente():
    nombre = str(input("Nombre: "))
    nif = str(input("DNI: "))
    direccion = str(input("Direccion: "))
    telefono = int(input("Telefono: "))
    correo = str(input("Correo: "))
    preferente = str(input("Preferente (s/n): "))

    if preferente == "s":
        preferente = True
    else:
        preferente = False

    if nif in diccionario_clientes:
        print("ERROR: ese cliente ya esta dado de alta en el sistema")
    else:
        diccionario_clientes.update({nif: {"nombre": nombre, "direccion": direccion, "telefono": telefono, "correo": correo, "preferente": preferente}})
        print "El cliente "+nombre+" con DNI '"+nif+"' ha sido dado de alta correctamente"

    print diccionario_clientes


def eliminar_cliente():
    cliente_eliminar = str(input("Introduce el DNI del cliente para eliminar: "))

    if cliente_eliminar in diccionario_clientes:
        del diccionario_clientes[cliente_eliminar]
        print "Se ha eliminado correctamente el cliente con DNI "+cliente_eliminar
    else:
        print "ERROR: El cliente con DNI '"+cliente_eliminar+"' no existe en el sistema"


def mostrar_cliente():
    cliente_mostrar = str(input("Introduce el DNI del cliente para mostrar: "))

    if cliente_mostrar in diccionario_clientes:
        datos_cliente = diccionario_clientes[cliente_mostrar]
        print "DNI: "+cliente_mostrar+" Nombre: "+datos_cliente["nombre"]+", Correo: "+datos_cliente["correo"]+", Telefono: "+str(datos_cliente["telefono"])+", Preferente: "+str(datos_cliente["preferente"])+", Direccion: "+datos_cliente["direccion"]
    else:
        print "El cliente con DNI '"+cliente_mostrar+"' no existe en el sistema"


def listar_clientes():
    mostrar_solo_preferentes = str(input("Quieres mostrar solo los clientes preferentes (s/n): "))

    if mostrar_solo_preferentes == "s":
        for i in diccionario_clientes.keys():
            datos_cliente = diccionario_clientes.get(i)
            if datos_cliente["preferente"]:
                print datos_cliente["nombre"]+" "+i
    else:
        for i in diccionario_clientes.keys():
            datos_cliente = diccionario_clientes.get(i)
            print datos_cliente["nombre"]+" "+i


def editar_cliente():
    cliente_editar = str(input("Introduce el DNI del cliente para editar: "))

    if cliente_editar in diccionario_clientes.keys():
        datos_cliente_editar = diccionario_clientes.get(cliente_editar)
        print "Datos cliente seleccionado '"+cliente_editar+"': 'nombre' -> "+datos_cliente_editar["nombre"]+" 'correo' -> "+datos_cliente_editar["correo"]+" 'telefono' -> "+str(datos_cliente_editar["telefono"])+" 'direccion' -> "+datos_cliente_editar["direccion"]+" 'preferente' -> "+str(datos_cliente_editar["preferente"])
        dato_modificar = str(input("Que dato quieres modificar: "))
        if dato_modificar in datos_cliente_editar:
            dato_modificado = str(input("Introduce el nuevo valor para '"+dato_modificar+"': "))
            datos_cliente_editar[dato_modificar] = dato_modificado
            diccionario_clientes[cliente_editar] = datos_cliente_editar
            print diccionario_clientes.get(cliente_editar)
        else:
            print "El dato '"+dato_modificar+"' no se ha encontrado"
    else:
        print "El cliente con DNI '"+cliente_editar+"' no existe en el sistema"

def mostrar_menu():
    print("----------------- MENU ------------------")
    print("1) Nuevo cliente      2) Eliminar cliente")
    print("3) Mostrar cliente    4) Listar clientes")
    print("5) Editar cliente     6) Salir")
    print("-----------------------------------------")


cerrar_programa = False

while not cerrar_programa:
    mostrar_menu()
    opcion_elegida = int(input("Selecciona una opcion: "))

    if opcion_elegida == 1:
        annadir_cliente()
    elif opcion_elegida == 2:
        eliminar_cliente()
    elif opcion_elegida == 3:
        mostrar_cliente()
    elif opcion_elegida == 4:
        listar_clientes()
    elif opcion_elegida == 5:
        editar_cliente()
    elif opcion_elegida == 6:
        cerrar_programa = True
    else:
        print "La opcion elegida no existe"

