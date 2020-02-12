#Escribir un programa que pida al usuario un numero entero y muestre por pantalla si es un numero primo o no

esPrimo = True
numero_introducido = int(input("Introduce un numero: "))

for i in range(numero_introducido-1, 1, -1):
    if numero_introducido % i == 0:
        esPrimo = False

if esPrimo:
    print("El numero "+str(numero_introducido)+" es primo")
else:
    print("El numero "+str(numero_introducido)+" no es primo")