#Escribir un programa que pregunte al usuario los numeros ganadores de la loteria primitiva, los almacene en una lista y los muestre por pantalla ordenados de menor a mayor

numero_ganador = 0
numeros_ganadores = []

print("Introduce los numeros ganadores de la loteria, para finalizar escribe '-1'")

while(numero_ganador != -1):
    numero_ganador = int(input("Numero premiado: "))

    if numero_ganador != -1:
        numeros_ganadores.append(numero_ganador)

numeros_ganadores.sort()
for i in range(len(numeros_ganadores)):
    print(numeros_ganadores[i])
