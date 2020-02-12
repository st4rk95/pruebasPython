#Escribir un programa en el que se pregunte al usuario por una frase y una letra y muestre por pantalla el numero de veces que aparece la letra en la frase

frase_introducida = str(input("Introduce una frase: "))
letra_buscar = str(input("Introduce una letra a buscar en la frase: "))

#Con funcion Python
print("(FUNCION) La letra '"+letra_buscar+"' aparece "+str(frase_introducida.count(letra_buscar))+" veces en la frase '"+frase_introducida+"'")

#Con bucle
contador_apariciones_letra = 0
for i in range(len(frase_introducida)):
   if frase_introducida[i] == letra_buscar:
       contador_apariciones_letra += 1

print("(BUCLE) La letra '"+letra_buscar+"' aparece "+str(contador_apariciones_letra)+" veces en la frase '"+frase_introducida+"'")