#--------------Ejercicio 4--------------

departamentos_colombia = []

num = int(input("Escriba número de departamentos de Colombia que desea ingresar "))

for x in range(num):

    dep = (input("Ingrese departamento:"))
    departamentos_colombia.append(dep)

print("Los últimos departamentos ingresados son: " ,{departamentos_colombia[-2]},{departamentos_colombia[-1]})

departamentos_colombia.sort(reverse=True)

dep_cont = len(departamentos_colombia)

#--------------Ejercicio 7--------------

print("La lista de departamentos es: " ,departamentos_colombia, "La lista tiene ",dep_cont, "departamentos" )

#print(f"Los departamentos son: {departamentos_colombia} y los ultimos dos departamentos ingresados son:")
