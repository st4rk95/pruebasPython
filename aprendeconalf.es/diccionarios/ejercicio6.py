#Escribir un programa que cree un diccionario vacio y lo vaya llenado con informacion sobre una persona (por ejemplo nombre, edad, sexo, telefono, correo electronico, etc.) que se le pida al usuario. Cada vez que se annada un nuevo dato debe imprimirse
# el contenido del diccionario.

diccionarioPersona = {}

nombre = str(input("Introduce tu nombre: "))
diccionarioPersona.update({"nombre": nombre})
print diccionarioPersona

edad = int(input("Introduce tu edad: "))
diccionarioPersona.update({"edad": edad})
print diccionarioPersona

telefono = int(input("Introduce tu telefono: "))
diccionarioPersona.update({"telefono": telefono})
print diccionarioPersona
