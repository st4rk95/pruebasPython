#Escribir un programa que pida al usuario una palabra y luego muestre por pantalla una a una las letras de la palabra introducida, empezando por la ultima

palabra_introducida = str(input("Introduce una palabra: "))

#Con funcion propia de Python
print(palabra_introducida[::-1])

#Con bucle
for i in range(len(palabra_introducida), 0, -1):
    print palabra_introducida[i-1]
