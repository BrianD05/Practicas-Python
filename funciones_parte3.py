"""numeros_positivos: Recibe un entero positivo. Retorna una lista que contiene todos los números positivos hasta llegar al número que recibió como parámetro.

Ejemplo:

    numeros_positivos(5) => [1,2,3,4,5]"""

def numero_positivos(numero):

    lista = []
    for i in range(1,numero + 1):

        lista.append(i)

    return lista    

print(numero_positivos(5)) 

"""numeros_positivos_pares: Recibe un entero positivo. Retorna una lista que contiene todos los números positivos pares hasta llegar al número que recibió como parámetro.

Ejemplo:

    numeros_positivos_pares(7) => [2,4,6]"""

def numeros_positivos_pares(numero):

    lista_pares = []

    for i in range(1,numero+1):

        if i % 2 == 0:

            lista_pares.append(i)

    return lista_pares

print(numeros_positivos_pares(7)) 

"""numeros_positivos_pares_cuadrado: Recibe un entero positivo. Retorna una lista que contiene todos los números positivos PARES elevados al cuadrado hasta llegar al número que recibió como parámetro.

Ejemplo:

    numeros_positivos_pares(7) => [4,16,36]"""

def numero_positivos_pares_cuadrado(numero):

    lista_al_cuadrado = []

    for k in range(1,numero + 1):

        if k % 2 == 0:
            lista_al_cuadrado.append(k**2)

    return lista_al_cuadrado

print(numero_positivos_pares_cuadrado(7))


"""impares_al_cuadrado: Recibe una lista de enteros positivos. Retorna una nueva lista donde los números impares están elevados al cuadrado, mientras que los pares se conservan sin sufrir ninguna modificación.

Ejemplo:

    impares_al_cuadrado([1,2,3,4,5,6,7]) => [1,2,9,4,25,6,49]"""

def impares_al_cuadrado(lista):

    lista_par_impar = []

    for i in lista:

        if i %2 !=0:
            lista_par_impar.append(i**2)

        else:
            lista_par_impar.append(i)

    return lista_par_impar

print(impares_al_cuadrado([1,2,3,4,5,6,7]))           

#-------------------------------------------ORDENAMIENTO----------------------------------------------------------


"""ordenar_lista_menor_a_mayor: Recibe una lista que contiene únicamente números. Retorna la lista ordenada de menor a mayor.

Ejemplo:

ordenar_lista_menor_a_mayor([5,2,6,23,4]) => [2,4,5,6,23]"""

def ordenar_lista_menor_a_mayor(lista):

    ordenado = sorted(lista)

    return ordenado

print(ordenar_lista_menor_a_mayor([5,2,6,23,4]))

"""ordenar_lista_mayor_a_menor: Recibe una lista que contiene únicamente números. Retorna la lista ordenada de mayor a menor.

Ejemplo:

ordenar_lista_menor_a_mayor([5,2,6,23,4]) => [23,6,5,4,2]
"""

def ordenar_lista_menor_a_mayor(lista):

    ordenamiento_menor_mayor = sorted(lista,reverse=True)

    return ordenamiento_menor_mayor

print(ordenar_lista_menor_a_mayor([5,2,6,23,4]))

"""ordenar_lista_alfabeticamente: Recibe una lista que contiene únicamente strings.
Retorna la lista ordenada alfabeticamente.

Ejemplo:

ordenar_lista_alfabeticamente(["hola", "estas", "como", "si"]) => ["como", "estas", "hola", "si"]"""

def ordenar_lista_alfabeticamente(lista):

    lista_ordenado = sorted(lista)

    return lista_ordenado
print(ordenar_lista_alfabeticamente(["hola", "estas", "como", "si"]))

"""ordenar_palabras_por_longitud: Recibe una lista que contiene únicamente strings. Retorna la lista ordenada en forma descendente (los mas grandes
en las primeras posiciones) según la longitud de cada string.

Ejemplo:

ordenar_palabras_por_longitud(["a", "hola", "si", "string largo", "string"]) => ["string largo", "string", "hola", "si", "a"]"""

def ordenar_palabras_por_longitud(lista):

    lista_ordenada = sorted(lista,key=len,reverse=True)

    return lista_ordenada

print(ordenar_palabras_por_longitud(["a", "hola", "si", "string largo", "string"]))


"""ultimos_tres_elementos: Recibe una lista previamente inicializada, de longitud mayor o igual a 3. Retorna una lista con los últimos tres elementos de la que se recibi.

Ejemplo:

ultimos_tres_elementos([5,3,6,2,5,32,6,4,7]) => [6,4,7]"""

def ultimos_tres_elementos(lista):

    ultimos_tres = lista[6:9]

    return ultimos_tres

print(ultimos_tres_elementos([5,3,6,2,5,32,6,4,7]))

"""ultimos_tres_elementos_concatenados: Recibe una lista de listas. Retorna una única lista que tiene concatenados los últimos tres elementos de cada una de las listas individuales en el orden original.

Ejemplo:

ultimos_tres_elementos_concatenados([[1,2,3,4], [5,6,7,8], [9,10,11,12]]) => [2,3,4, 6,7,8,10,11,12]"""

def ultimos_tres_elementos_concatenados(lista):

    lista_nueva = []
    
    for i in lista:
       lista_nueva.extend(i[-3::])
       
    return lista_nueva 

print(ultimos_tres_elementos_concatenados([[1,2,3,4], [5,6,7,8], [9,10,11,12]]))
        

"""indices_pares: Recibe una lista previamente inicializada. Retorna una lista que tiene únicamente los elementos correspondientes a los índices pares de la lista que recibió como parámetro.

Hint: Recordar que los índices comienzan en 0.

Ejemplo:

indices_pares(["a","b","c","d","e"]) -> ["a","c","e"]"""

def indices_pares(lista):

    indicar_pares = lista[0::2]

    return indicar_pares

print(indices_pares(["a","b","c","d","e"]))

"""indices_impares: Recibe una lista previamente inicializada. Retorna una lista que tiene únicamente los elementos correspondientes a los índices impares de la lista que recibió como parámetro.

Ejemplo:

indices_pares(["a","b","c","d","e", "f"]) -> ["b","d","f"]"""


def indices_impares(lista):

    indices_impares1 = lista[1::2]

    return indices_impares1

print(indices_impares(["a","b","c","d","e", "f"]))

"""invertir: Recibe una lista previamente inicializada. Retorna dicha lista invertida.

Ejemplo:

invertir([1,2,3,4,5]) => [5,4,3,2,1]"""

def invertir(lista):

    lista_invertida = sorted(lista,reverse=True)

    return lista_invertida

print(invertir([1,2,3,4,5]) )


      

