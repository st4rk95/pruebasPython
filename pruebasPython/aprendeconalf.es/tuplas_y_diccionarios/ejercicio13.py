#Escribir un programa que pregunte por una muestra de numeros, separados por comas, los guarde en una lista y muestre por pantalla su media

numeros_introducidos = str(input("Introduce una serie de numeros separados por comas: "))

lista_numeros = numeros_introducidos.split(",")
suma_total = 0

for i in lista_numeros:
    suma_total += int(i)

print ("En la lista hay "+str(len(lista_numeros))+" numeros, que suman un total de "+str(suma_total)+", por lo que la media aritmetica es "+str(suma_total/len(lista_numeros)))
