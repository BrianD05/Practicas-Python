"""numeros_al_cuadrado: Recibe un numero entero positivo. Retorna un diccionario cuya claves comprenden el rango de números positivos tomando como límite superior el número que se recibió como parámetro, y donde para cada clave su valor asociado será el número de la clave al cuadrado.

Ejemplo:

    numeros_al_cuadrado(4) => {1: 1, 2: 4, 3: 9, 4: 16}"""

def numeros_al_cuadrado(numero):

    return {x: x**2 for x in range(1,numero + 1)}

print(numeros_al_cuadrado(4))

"""mezclar_diccionarios: Recibe dos diccionarios. Retorna un único diccionario, que resulta de realizar la mezcla entre los dos. Las claves del nuevo diccionario deben ser las claves de ambos (asumir que no tienen claves iguales), con sus respectivos valores.

Ejemplo:

    dicc_1 = {'clave1': 1, 'clave3': 3}
    dicc_2 = {'clave2': 2, 'clave4': valor4}

    numeros_al_cuadrado(dicc_1, dicc_2) => 

           {'clave1': 1, 'clave3': 3, 'clave2': 2, 'clave4': 4}
Aclaración: El orden de los pares asociados clave-valor puede ser cualquiera."""


def mezclar_diccionarios(dicc_uno, dicc_dos):
    
    resultadox = dicc_uno.copy()
    resultadox.update(dicc_dos)
    
    return resultadox
dicc_1 = {'clave1': 1, 'clave3': 3}
dicc_2 = {'clave2': 2, 'clave4': 4}
print(mezclar_diccionarios(dicc_1,dicc_2))

"""filtrar_por_sumar_diez: Recibe un diccionario cuyas claves son enteros, y también su valor asociado. Retorna un diccionario que contiene únicamente los pares clave-valor del diccionario que se recibió por parámetro que al sumarlos sean mayores o iguales a 10.

Ejemplo:

   filtrar_por_sumar_diez({8: 11, 3: 6, 9: 2, 1: 4}) => {8: 11, 9: 2}"""

def filtrar_por_sumar_diez(diccionario):
    diccionario_nuevo = {}
    for key,values in diccionario.items():
        
        if key + values >=10:
            
            diccionario_nuevo[key] = values
            
    return diccionario_nuevo

print(filtrar_por_sumar_diez(filtrar_por_sumar_diez({8: 11, 3: 6, 9: 2, 1: 4})))

"""ordenar_valores_por_longitud: Recibe un diccionario con claves de tipo string y valores asociados de tipo string. Retorna una lista ordenada que contiene únicamente los valores del diccionario. Esta lista debe estar ordenada descendentemente (mayor a menor) según la longitud que tienen las cadenas de caracteres que son valor.

Ejemplo:

   dicc = {'boca':'river', 'pablo':'guarna', 'hola':'algoritmos'}
   ordenar_valores_por_longitud(dicc) => ['algoritmos','guarna','river']"""

def ordenar_valores_por_longitud(diccionario):
    
    valores_dicc= list(diccionario.values())
    nueva_variable = sorted(valores_dicc,key=len,reverse=True)
    
    return nueva_variable


#------------------------------PRACTICA NUEVAMENTE DE DICCIONARIO----------------------------------------------


"""numeros_al_cuadrado: Recibe un numero entero positivo. Retorna un diccionario cuya claves comprenden el rango de números positivos tomando como límite superior el número que se recibió como parámetro, y donde para cada clave su valor asociado será el número de la clave al cuadrado.

Ejemplo:

    numeros_al_cuadrado(4) => {1: 1, 2: 4, 3: 9, 4: 16}"""


def numeros_al_cuadrado(numero):


    return {x:x**2 for x in range(1,numero + 1)}


print(numeros_al_cuadrado(4))


"""mezclar_diccionarios: Recibe dos diccionarios. Retorna un único diccionario, que resulta de realizar la mezcla entre los dos. Las claves del nuevo diccionario deben ser las claves de ambos (asumir que no tienen claves iguales), con sus respectivos valores.

Ejemplo:

    dicc_1 = {'clave1': 1, 'clave3': 3}
    dicc_2 = {'clave2': 2, 'clave4': valor4}

    numeros_al_cuadrado(dicc_1, dicc_2) => 

           {'clave1': 1, 'clave3': 3, 'clave2': 2, 'clave4': 4}
Aclaración: El orden de los pares asociados clave-valor puede ser cualquiera."""


def mezclar_diccionarios(dicc1,dicc2):

    resultado = dicc1.copy()
    resultado.update(dicc2)

    return resultado

dicc_1 = {'clave1': 1, 'clave3': 3}
dicc_2 = {'clave2': 2, 'clave4': 4}
mezcla = mezclar_diccionarios(dicc_1,dicc_2)
print(mezcla)


"""filtrar_por_sumar_diez: Recibe un diccionario cuyas claves son enteros, y también su valor asociado. Retorna un diccionario que contiene únicamente los pares clave-valor del diccionario que se recibió por parámetro que al sumarlos sean mayores o iguales a 10.

Ejemplo:

   filtrar_por_sumar_diez({8: 11, 3: 6, 9: 2, 1: 4}) => {8: 11, 9: 2}"""

def filtrar_por_sumar_diez(diccionario):

    diccionario_nuevo = {}

    for key,values in diccionario.items():

        if key + values >=10:
            diccionario_nuevo[key]=values

    return diccionario_nuevo

print(filtrar_por_sumar_diez({8: 11, 3: 6, 9: 2, 1: 4}))        


"""ordenar_valores_por_longitud: Recibe un diccionario con claves de tipo string y valores asociados de tipo string. Retorna una lista ordenada que contiene únicamente los valores del diccionario. Esta lista debe estar ordenada descendentemente (mayor a menor) según la longitud que tienen las cadenas de caracteres que son valor.

Ejemplo:

   dicc = {'boca':'river', 'pablo':'guarna', 'hola':'algoritmos'}
   ordenar_valores_por_longitud(dicc) => ['algoritmos','guarna','river']"""


def ordenar_valores_por_longitud(dicc):

    valores_diccionario = list(dicc.values())

    ordenar_lista = sorted(valores_diccionario,key=len,reverse=True)

    return ordenar_lista

dicc = {'boca':'river', 'pablo':'guarna', 'hola':'algoritmos'}
print(ordenar_valores_por_longitud(dicc))

#--------------------------------------Mas ejercicios de funciones de diccionario----------------------------


"""numeros_al_cuadrado: Recibe un numero entero positivo. Retorna un diccionario cuya claves comprenden el rango de números positivos tomando como límite superior el número que se recibió como parámetro, y donde para cada clave su valor asociado será el número de la clave al cuadrado.

Ejemplo:

    numeros_al_cuadrado(4) => {1: 1, 2: 4, 3: 9, 4: 16}"""


def numeros_al_cuadrado(numero):

    return {x:x**2 for x in range(1,numero + 1)}


print(numeros_al_cuadrado(4))

"""mezclar_diccionarios: Recibe dos diccionarios. Retorna un nuevo y único diccionario, que resulta de realizar la mezcla entre los dos. Las claves del nuevo diccionario deben ser las claves de ambos. Las claves pueden estar repetidas, en ese caso, deberían sumar sus respectivos valores.

Ejemplo:

    dicc_1 = {'clave1': 1, 'clave3': 3}
    dicc_2 = {'clave2': 2, 'clave3': 2, 'clave4': 4}

    mezclar_diccionarios(dicc_1, dicc_2) => 

           {'clave1': 1, 'clave3': 5, 'clave2': 2, 'clave4': 4}
Aclaración: El orden de los pares asociados clave-valor puede ser cualquiera."""

def mezclar1_diccionario(dicc_1,dicc_2):

    resultado = dicc_1.copy()
    resultado.update(dicc_2)

    return resultado

dicc_1 = {'clave1': 1, 'clave3': 3}
dicc_2 = {'clave2': 2, 'clave3': 2, 'clave4': 4}
print(mezclar1_diccionario(dicc_1,dicc_2))

"""filtrar_por_sumar_diez: Recibe un diccionario cuyas claves son enteros, y también su valor asociado. Retorna un diccionario que contiene únicamente los pares clave-valor del diccionario que se recibió por parámetro que al sumarlos sean mayores o iguales a 10.

Ejemplo:

   filtrar_por_sumar_diez({8: 11, 3: 6, 9: 2, 1: 4}) => {8: 11, 9: 2}"""

def filtrar_por_sumar_diez(diccionario1):

    diccionario_nuevo1 = {}

    for key,values in diccionario1.items():

        if key + values >= 10:

            diccionario_nuevo1[key] = values

    return diccionario_nuevo1


print(filtrar_por_sumar_diez({8: 11, 3: 6, 9: 2, 1: 4}))

"""ordenar_valores_por_longitud: Recibe un diccionario con claves de tipo string y valores asociados de tipo string. Retorna una lista ordenada que contiene únicamente los valores del diccionario. Esta lista debe estar ordenada descendentemente (mayor a menor) según la longitud que tienen las cadenas de caracteres que son valor.

Ejemplo:

   dicc = {'boca':'river', 'julian':'ruiz', 'hola':'algoritmos'}
   ordenar_valores_por_longitud(dicc) => ['algoritmos','river', 'ruiz']"""


def ordenar_valores_por_longitud(dicc):

    valores_diccionario = list(dicc.values())

    resultado = sorted(valores_diccionario,key=len,reverse=True)


    return resultado
dicc = {'boca':'river', 'julian':'ruiz', 'hola':'algoritmos'}
print(ordenar_valores_por_longitud(dicc))