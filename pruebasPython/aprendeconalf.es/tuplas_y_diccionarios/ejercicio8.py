#Escribir un programa que pida al usuario una palabra y muestre por pantalla si es un palindromo

palabra_introducida = str(input("Introduce una palabra: "))

if palabra_introducida == palabra_introducida[::-1]:
    print "Es un palindromo"
else:
    print "No es un palindromo"


