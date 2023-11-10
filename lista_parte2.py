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


#Duplicar valores: Dada una lista de números, crea una nueva lista que contenga cada número duplicado

numeros = [1,2,3,4,5,6,7,8,9,10]

numeros_duplicados = []

for i in numeros:

    numeros_duplicados.append(i)
    numeros_duplicados.append(i)

print(numeros_duplicados)

#Eliminar elementos impares: Elimina todos los elementos impares de una lista de números.

numeros1 = [2, 5, 8, 11, 14, 17, 20, 23, 26, 29, 32, 35, 38, 41, 44, 47, 50, 53, 56, 59]

numeros_pares = []

for i in numeros1:

    if i % 2==0:

        numeros_pares.append(i)

print(numeros_pares)

#Multiplicación de elementos: Dada una lista de números, crea una nueva lista que contenga cada número multiplicado por un valor específico.

numeros3 = [10, 23, 7, 45, 12, 88, 34, 56, 2, 19, 5, 67, 3, 27, 50, 8, 61, 14, 32, 76, 9, 42, 68, 1, 77, 51, 28, 6, 94, 17]

numeros_multiplicados = []

for k in numeros3:

    multiplicacion = k * 5

    numeros_multiplicados.append(multiplicacion)

print(numeros_multiplicados)   

#Lista de cuadrados: Dada una lista de números, crea una nueva lista que contenga los cuadrados de los números.

numeros4 = [42, 15, 7, 88, 12, 19, 32, 60, 25, 53, 6, 11, 99, 36, 29, 18, 51, 77, 21, 5, 63, 2, 8, 44, 1, 67, 40, 3, 54, 72, 48, 9, 64, 17, 35, 55, 22, 14, 70, 20, 58, 16, 23, 26, 13, 38, 49, 30, 41, 10, 47, 68, 4, 31, 50, 24, 61, 76, 33, 27, 52, 39, 62, 91, 43, 80, 37, 65, 46, 75, 83, 59, 45, 85]

numeros_al_cuadrado = []
for cuadrado in numeros4:

     numero_cuadrado = cuadrado ** 2

     numeros_al_cuadrado.append(numero_cuadrado)

print(numeros_al_cuadrado)     

#Promedio de elementos pares: Calcula el promedio de todos los elementos pares en una lista de números.

numeros5 = [5, 8, 12, 2, 11, 14, 7, 9, 6, 1, 13, 4, 10, 3, 15]

promedio = sum(numeros5) / len(numeros5) 

print(f"El promedio es {promedio}")

#Otra forma de hacerlo

suma_numero_lista = 0
contador = 0

for i in numeros5:

    suma_numero_lista+=i
    contador +=1

promedio2 = suma_numero_lista / contador



print(f"El promedio dos es {promedio2}")

#Mayor diferencia: Encuentra la mayor diferencia entre dos elementos en una lista de números.

lista_numeros = [10, 5, 8, 3, 12, 7, 15, 20, 18, 25]

mayor_diferencia = max(lista_numeros) - min(lista_numeros)

print(mayor_diferencia)


#Suma acumulativa: Crea una nueva lista que contenga la suma acumulativa de los elementos de una lista dada.

numero_lista = [10, 5, 8, 3, 12, 7, 15, 20, 18, 25]

suma_acumulativa = []

suma_temporal = 0

for k in numero_lista:

    suma_temporal +=k
    suma_acumulativa.append(suma_temporal)

print(suma_acumulativa)

#Ordenar lista de cadenas: Dada una lista de cadenas, ordénalas alfabéticamente.

lista_cadenas = ["manzana", "banana", "uva", "kiwi", "pera", "naranja", "fresa", "mango", "cereza", "piña"]


lista_ordenada = sorted(lista_cadenas)

print(lista_ordenada)


#Lista de elementos únicos: Dada una lista con elementos repetidos, crea una nueva lista que contenga solo los elementos únicos en el mismo orden en que aparecen.

lista_repetida = [1, 2, 2, 3, 4, 4, 5, 1, 6, 7, 8, 9, 9, 10]

lista_sin_repetir = list(set(lista_repetida))

print(lista_sin_repetir)










