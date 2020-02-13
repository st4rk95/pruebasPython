#Escribir un programa que pregunte al usuario su nombre, edad, direccion y telefono y lo guarde en un diccionario. Despues debe mostrar por pantalla el mensaje <nombre> tiene <edad> annos, vive en <direccion> y su numero de telefono es <telefono>.

diccionarioPersona = {}
nombre = str(input("Introduce tu nombre: "))
edad = int(input("Introduce tu edad: "))
direccion = str(input("Introduce tu direccion: "))
telefono = int(input("Introduce tu telefono: "))

actualizar_diccionario = {"nombre": nombre, "edad": edad, "direccion": direccion, "telefono": telefono}

diccionarioPersona.update(actualizar_diccionario)

print diccionarioPersona