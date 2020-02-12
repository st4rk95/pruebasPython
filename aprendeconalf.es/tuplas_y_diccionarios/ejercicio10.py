#Escribir un programa que almacene en una lista los siguientes precios, 50, 75, 46, 22, 80, 65, 8, y muestre por pantalla el menor y el mayor de los precios.

listaPrecios = [50, 75, 46, 22, 80, 65, 8]
listaPrecios.sort()
print("El precio mas bajo es "+str(listaPrecios[0]))
print("El precio mas bajo es "+str(listaPrecios[len(listaPrecios)-1]))

