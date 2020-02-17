#Escribir un programa que cree un diccionario simulando una cesta de la compra. El programa debe preguntar el articulo y su precio y annadir el par al diccionario, hasta que el usuario decida terminar.
# Despues se debe mostrar por pantalla la lista de la compra y el coste total

diccionarioCestaCompra = {}

salir = False
precioTotal = 0

while not salir:
    producto = str(input("Introduce un producto para annadir a la cesta: "))
    precio = float(input("Introduce el precio del producto: "))

    if producto in diccionarioCestaCompra:
        precio += diccionarioCestaCompra.get(producto)

    diccionarioCestaCompra.update({producto: precio})

    salir = str(input("Quieres annadir mas productos a la cesta s/n: "))

    if salir == "s":
        salir = False
    else:
        salir = True

salir = False

while not salir:
    salir = str(input("Quieres eliminar algun producto de la cesta s/n: "))
    if salir == "s":
        salir = False
        producto_eliminar = str(input("Escribe el producto que quieres eliminar: "))
        if producto_eliminar in diccionarioCestaCompra:
            del diccionarioCestaCompra[producto_eliminar]
            print "Se ha eliminado '"+producto_eliminar+"' de la lista de la compra"
        else:
            print "El producto seleccionado no se encuentra en la lista de la compra"
    else:
        salir = True


print "Lista de la compra"
for i in diccionarioCestaCompra.keys():
    precioTotal += diccionarioCestaCompra.get(i)
    print(i+"        "+str(diccionarioCestaCompra.get(i)))

print ("El precio total de los productos es "+str(precioTotal))