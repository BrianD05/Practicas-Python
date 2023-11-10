#Crear una tupla con elementos:

tupla = (1,2,3,"Hola","Mundo")
print(tupla)

#Acceder al tercer elemento de una tupla:

tupla = (10, 20, 30, 40, 50)

tercer_elemento = tupla[2]

print(tercer_elemento)

#Concatenar dos tuplas:

tupla1 = (1, 2, 3)
tupla2 = (4, 5, 6)

concatenar_tupla = tupla1 + tupla2

print(concatenar_tupla)

#Imprimir todos los elementos de una tupla usando un bucle for:

tupla = (10, 20, 30, 40, 50)

for i in tupla:

    print(i)

#Encontrar la longitud de una tupla:

tupla = (1, 2, 3, 4, 5)

longitud = len(tupla)

print(longitud)

#Verificar si un elemento está presente en una tupla:

tupla = (10, 20, 30, 40, 50)
elemento_a_buscar = 60

elemento_en_tupla = elemento_a_buscar in tupla

print(elemento_en_tupla)

#Contar cuántas veces aparece un elemento en una tupla:

tupla1 = (1, 2, 2, 3, 2, 4, 2, 5)

contador = tupla1.count(2)

print(contador)

#Encontrar el índice de un elemento en una tupla:

tupla3 = ('a', 'b', 'c', 'd', 'e')

indice = tupla3.index("b")

print(indice)

#Crear una tupla de tuplas e imprimir cada elemento:

tuplas_anidadas = ((1, 2, 3), (4, 5, 6), (7, 8, 9))

for elemento in tuplas_anidadas:

    for tupla in elemento:

        print(tupla)