#Escribir un programa que pida al usuario un numero entero positivo y muestre por pantalla la cuenta atras desde ese numero hasta cero
numero_introducido = int(input("Introduce in numero entero positivo: "))

for i in range(numero_introducido,-1,-1):
    print(i)