#Ejercicio 1
#Escribir un programa que almacene las asignaturas de un curso (por ejemplo Matemáticas, Física, Química, Historia y Lengua) en una lista y la muestre por pantalla.

lista = ["Matematicas","Fisica","Quimica","Historia","Lengua"]

print(lista)

#Ejercicio 2
# Escribir un programa que almacene las asignaturas de un curso (por ejemplo Matemáticas, Física, Química, Historia y Lengua) en una lista y la muestre por pantalla el mensaje Yo estudio <asignatura>, donde <asignatura> es cada una de las asignaturas de la lista.

lista2 = ["Matematicas","Fisica","Quimica","Historia","Lengua"]

for i in lista2:

    print(f"Yo estudio {i}")

#Ejercicio 3
# Escribir un programa que almacene las asignaturas de un curso (por ejemplo Matemáticas, Física, Química, Historia y Lengua) en una lista, pregunte al usuario la nota que ha sacado en cada asignatura, y después las muestre por pantalla con el mensaje En <asignatura> has sacado <nota> donde <asignatura> es cada una de las asignaturas de la lista y <nota> cada una de las correspondientes notas introducidas por el usuario.    


materias = ["Matematicas","Fisica","Quimica","Historia","Lengua"]

notas_lista = []

for i in materias:

    notas = int(input(f"Que notas sacaste en {i}: "))

    notas_lista.append(notas)


for j in range(len(materias)):

    print(f"La nota que sacaste en {materias[j]} es {notas_lista[j]} ")  



#Ejercicio 4
#Escribir un programa que pregunte al usuario los números ganadores de la lotería primitiva, los almacene en una lista y los muestre por pantalla ordenados de menor a mayor.

numero_loteria = []

for i in range(1,7):
    ingresar_numeros = int(input("Ingrese los numeros ganadores de la loteria: "))
    numero_loteria.append(ingresar_numeros)

numero_loteria.sort()
for j in numero_loteria:

    print(j)

#Crea una lista que contenga los nombres de tus amigos. Luego, imprime la lista de nombres.

lista_amigos = ["Brian","Fulano","Megano","Firulais"]

print(lista_amigos)
#Define una tupla con los meses del año. Luego, imprime el tercer mes.

tupla_meses = ("Enero","Febrero","Marzo","Abril","Mayo","Junio","Julio","Agosto","Septiembre","Octubre","Noviembre","Diciembre")

print(tupla_meses[2])




