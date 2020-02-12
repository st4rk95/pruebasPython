#Escribir un programa que muestre por pantalla la tabla de multiplicar del 1 al 10

for i in range(10):
    print("-------")
    print(i+1)
    print("-------")
    for j in range(10):
        print(str((i+1))+" x "+str((j+1))+" = "+str((j+1)*(i+1)))
