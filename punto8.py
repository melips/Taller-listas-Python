#--------------Ejercicio 8--------------

numeros = []

for i in range(0,5):

    num = int(input("ingrese un numero: "))

    if num in numeros:
        print("Número agregado a la lista")

    else:
        numeros.append(num)
        asc = sorted(numeros)
        des = sorted(numeros,reverse=True)
    
print("Lista de números ascendentes",asc)
print("Lista de números descendentes",des)
