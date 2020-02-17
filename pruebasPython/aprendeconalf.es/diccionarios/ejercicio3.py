#Escribir un programa que guarde en un diccionario los precios de las frutas de la tabla, pregunte al usuario por una fruta, un numero de kilos y muestre por pantalla el precio de ese numero de kilos de fruta. Si la fruta no esta en el diccionario debe mostrar un mensaje informando de ello.
#Fruta	   Precio
#Platano	1.35
#Manzana	0.80
#Pera	    0.85
#Naranja	0.70


diccionarioFrutas = {"Platano": 1.35, "Manzana": 0.8, "Pera": 0.85, "Naranja": 0.7}

fruta_elegida = str(input("Introduce una fruta para comprar: "))

if fruta_elegida in diccionarioFrutas:
    peso_elegido = float(input("Introduce cuantos kilos vas a comprar de "+fruta_elegida+": "))
    print("Precio total "+str(diccionarioFrutas.get(fruta_elegida)*peso_elegido)+" euros")
else:
    print "La fruta seleccionada no existe"

