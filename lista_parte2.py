#Suma de elementos: Escribe un programa que sume todos los elementos de una lista.

lista_numeros = [1,2,3,22,33,22,11,23,44,55,66,7,3,2,9,2,1,5,6,7,4,3,2]
suma = 0
for i in lista_numeros:

    suma+=i

print(f"La suma de los numero de la lista es {suma}")

#Otra forma de hacerlo mas resumido es
print(sum(lista_numeros))

#Números pares: Dada una lista de números, crea una nueva lista que contenga solo los números pares.

lista_numeros = [12, 45, 67, 89, 23, 56, 78, 34, 90, 1, 99, 43, 76, 54, 21]

lista_pares = []


for i in lista_numeros:

    if i %2==0:
        lista_pares.append(i)


print(lista_pares)    


#Eliminar duplicados: Elimina los elementos duplicados de una lista.

mi_lista = [1, 2, 2, 3, 4, 4, 5]

eliminar_duplicados = set(mi_lista)

convertir_a_lista = list(eliminar_duplicados)

print(convertir_a_lista)

#Ordenar lista: Ordena una lista de números de menor a mayor.

numeros = [17, 5, 12, 33, 8, 19, 24, 7, 15, 10, 1, 29, 4, 11, 22, 6, 16, 20, 3, 14]

ordenado = sorted(numeros,reverse=False)

print(ordenado)

#Lista inversa: Invierte una lista, de modo que el primer elemento se convierte en el último y viceversa.

numeros = [12, 45, 67, 89, 23, 56, 78, 34, 90, 1, 99, 43, 76, 54, 21, 8, 19, 33, 61, 25, 4, 58, 32, 14, 70, 5, 92, 36, 30, 7, 49, 63, 18, 26, 72, 39, 11, 83, 22, 46, 68, 17, 97, 40, 2, 55, 71, 9, 84]

lista_inversa = sorted(numeros,reverse=True)

print(lista_inversa)

#Concatenar listas: Combina dos listas en una sola.

lista1 = [15, 28, 42, 9, 11, 36, 5, 17, 20, 7]

lista2 = [8, 33, 14, 22, 3, 19, 25, 10, 12, 6]

lista_combinada = lista1 + lista2

print(lista_combinada)

#Conteo de elementos: Cuenta cuántas veces aparece un elemento específico en una lista.

lista = [2,3,4,2,3,4,2,3,4,1,2,3,4]

elemento_a_contar = 2

conteo = lista.count(elemento_a_contar)

print(conteo)

#Mayor y menor: Encuentra el valor máximo y mínimo en una lista de números.

numeros = [42, 15, 7, 88, 12, 19, 32, 60, 25, 53, 6, 11, 99, 36, 29, 18, 51, 77, 21, 5, 63, 2, 8, 44, 1, 67, 40, 3, 54, 72, 48, 9, 64, 17, 35, 55, 22, 14, 70, 20, 58, 16, 23, 26, 13, 38, 49, 30, 41, 10, 47, 68, 4, 31, 50]

maximo = max(numeros)
minimo = min(numeros)

print(f"El Maximo es {maximo} y el Minimo es {minimo}")




    