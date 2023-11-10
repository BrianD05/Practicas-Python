estudiantes = {
    "Juan": 25,
    "María": 30,
    "Pedro": 22,
    "Ana": 28,
    "Luis": 35
}

"""Imprime la edad de "Pedro".
   Añade a "Marta" con una edad de 27 al diccionario.
   Imprime todas las claves del diccionario.
   Calcula el promedio de edades de los estudiantes"""

edad = estudiantes["Pedro"]

print(edad)

estudiantes["Marta"] = 27

print(estudiantes)

promedio = sum(estudiantes.values()) / len(estudiantes)

print(promedio)


inventario = {
    "manzanas": 50,
    "plátanos": 30,
    "peras": 40,
    "naranjas": 25
}


"""Imprime la cantidad de "plátanos" en el inventario.
    Agrega 20 "uvas" al inventario.
    Actualiza la cantidad de "manzanas" a 60.
    Imprime todos los productos cuya cantidad sea superior a 35."""


cantidad_platanos = inventario["plátanos"]

print(cantidad_platanos)

inventario["uvas"] = 20

inventario["manzanas"] = 60

print(inventario)

for i,k in inventario.items():

    if k > 35:

        print(f"{i}: {k}")

calificaciones = {
    "Juan": 90,
    "María": 85,
    "Pedro": 78,
    "Ana": 92,
    "Luis": 88
}

"""Imprime todas las calificaciones en formato "Nombre: Calificación".
Añade a "Marta" con una calificación de 95 al diccionario.
Encuentra y imprime el estudiante con la calificación más alta.
Calcula el promedio de calificaciones."""

for nombre,calificacion in calificaciones.items():

    print(f"{nombre}: {calificacion}")

calificaciones["Marta"] = 95

estudiante = max(calificaciones,key=lambda k:calificaciones[k])

print(f"La estudiante con mayor nota es {estudiante}")

promedio2 = sum(calificaciones.values()) / len(calificaciones)

print(promedio2)



#PARTE 2


ventas_diarias = {
    "lunes": 150,
    "martes": 200,
    "miércoles": 180,
    "jueves": 250,
    "viernes": 220
}

"""Imprime el total de las ventas de la semana.
Encuentra el día con las ventas más altas.
Añade las ventas del "sábado" y "domingo" (100 cada uno) al diccionario.
Calcula el promedio de ventas diarias."""


suma = sum(ventas_diarias.values())

print(suma)



dia = max(ventas_diarias,key=lambda x:ventas_diarias[x])

print(dia)

ventas_diarias.update({"Sabado":100,"Domingo":100})

print(ventas_diarias)

promedio_diario = sum(ventas_diarias.values()) / len(ventas_diarias)

print(promedio_diario)

horas_trabajo = {
    "Juan": 40,
    "María": 35,
    "Pedro": 38,
    "Ana": 42,
    "Luis": 37
}

"""Imprime las horas que trabajó "Pedro".
Añade a "Marta" con 45 horas de trabajo al diccionario.
Encuentra al empleado que trabajó menos horas.
Calcula el total de horas trabajadas por todos los empleados."""

hora_trabajo_pedro = horas_trabajo["Pedro"]

print(hora_trabajo_pedro)

horas_trabajo["Marta"] = 45

empleado_menos_horas = min(horas_trabajo,key=lambda j:horas_trabajo[j])

print(empleado_menos_horas)

suma_trabajadas = sum(horas_trabajo.values())

print(suma_trabajadas)

precios_productos = {
    "manzanas": 2.5,
    "plátanos": 1.8,
    "peras": 3.0,
    "naranjas": 2.2
}

"""Imprime el precio de las "peras".
Añade "uvas" con un precio de 4.5 al diccionario.
Actualiza el precio de las "manzanas" a 3.0.
Calcula el total de gastos si compras 2 kg de cada producto."""

peras = precios_productos["peras"]

print(peras)

precios_productos["Uvas"] = 4.5

precios_productos["manzanas"] = 3.0

total_compradas = sum(precios_productos.values()) *2

print(total_compradas)