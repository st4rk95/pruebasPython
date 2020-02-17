#Escribir un programa que cree un diccionario de traduccion espannol-ingles. El usuario introducira las palabras en espannol e ingles separadas por dos puntos, y cada par <palabra>:<traduccion> separados por comas.
# El programa debe crear un diccionario con las palabras y sus traducciones. Despues pedira una frase en espannol y utilizara el diccionario para traducirla palabra a palabra. Si una palabra no esta en el diccionario debe dejarla sin traducir.

diccionarioTraductor = {}
frase_traducida = ""
salir = False

while not salir:

    palabra_esp = str(input("Introduce una palabra en castellano: "))
    palabra_eng = str(input("Introduce la traduccion en ingles para '"+palabra_esp+"': "))

    diccionarioTraductor.update({palabra_esp: palabra_eng})

    salir = str(input("Quieres annadir mas palabras al diccionario s/n: "))

    if salir == "s":
        salir = False
    else:
        salir = True


frase_traducir = str(input("Introduce una frase para traducir: "))
frase_traducir_split = frase_traducir.split(" ")

for i in frase_traducir_split:
    if i in diccionarioTraductor:
        frase_traducida += " "+diccionarioTraductor.get(i)
    else:
        frase_traducida += " "+i

print frase_traducida
print diccionarioTraductor