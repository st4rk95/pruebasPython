#Escribir un programa que pida al usuario un numero entero y muestre por pantalla un triangulo rectangulo como el de mas abajo, de altura el numero introducido

numero_introducido = int(input("Introduce un numero: "))

for i in range(1,numero_introducido+1):
    print ("*"*i)
