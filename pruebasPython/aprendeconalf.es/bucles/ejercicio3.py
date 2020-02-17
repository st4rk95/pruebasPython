#Escribir un programa que pida al usuario un numero entero positivo y muestre por pantalla todos los numeros impares desde 1 hasta ese numero separados por comas

numero_introducido = int(input("Introduce un numero: "))

for i in range(1, numero_introducido+1, 2):
    print i
