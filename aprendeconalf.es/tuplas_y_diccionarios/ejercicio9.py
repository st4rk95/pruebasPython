# Escribir un programa que pida al usuario una palabra y muestre por pantalla el numero de veces que contiene cada vocal

vocales = {"a": 0, "e": 0, "i": 0, "o": 0, "u": 0}

palabra_introducida = str(input("Introduce una palabra: "))

for i in range(len(palabra_introducida)):

    if palabra_introducida[i] in vocales:
        actualizarDiccionario = {palabra_introducida[i]: (vocales.get(palabra_introducida[i])+1)}
        vocales.update(actualizarDiccionario)

for i in vocales.keys():
    print("La palabra "+palabra_introducida+" contiene "+str(vocales.get(i))+" '"+i+"'")