"""Completar el cuerpo de la función. La misma debe devolver True en caso en el que el número recibido como parámetro recibido sea par, y False en caso contrario.

Ejemplos:

es_par(2) => True
es_par(3) => False
es_par(32) => True
es_par(33) => False"""


def es_par(numero):
    
    if (numero % 2 == 0):
        par = True
    else:
        par = False
    return par

print(es_par(2))
print(es_par(3)) 
print(es_par(32))
print(es_par(33))


"""Completar el cuerpo de la función. La misma debe devolver True en caso de que el número que se recibe como parámetro sea primo, y False en caso contrario.

Ejemplos:

es_primo(3) => True
es_primo(4) => False
es_primo(11) => True
es_primo(15) => False"""

def es_primo(numero):
    if numero < 2:
        return False  

    for i in range(2, int(numero**0.5) + 1):
        if numero % i == 0:
            return False  

    return True  


print(es_primo(3))  
print(es_primo(4))   
print(es_primo(11)) 
print(es_primo(15))  


"""Completar el cuerpo de la función. La misma recibe un número como parámetro y debe devolver el valor absoluto del mismo.

Ejemplos:

valor_absoluto(3) => 3
valor_absoluto(-3) => 3"""


def valor_absoluto(numero):
    

    valor_absoluto = abs(numero)

    return valor_absoluto

resultado = valor_absoluto(3)
resultado1 = valor_absoluto(-3)

print(resultado)
print(resultado1)

"""Completar el cuerpo de la función. La misma recibe tres cadenas previamente inicializadas y debe retornar la suma de la longitud de la concatenación de las tres cadenas.

Ejemplo:

    longitud_cadenas("hola", "como", "estas") => 13
    longitud_cadenas("a", "b", "c") => 3"""


def longitud_cadenas(cadena1,cadena2,cadena3):

    concatenacion = cadena1 + cadena2 + cadena3

    longitud_cadenas1 = len(concatenacion)

    return longitud_cadenas1

print(longitud_cadenas("hola", "como", "estas"))
print(longitud_cadenas("a", "b", "c"))

"""Completar el cuerpo de la función. La misma recibe una cadena de caracteres y dos caracteres individuales. Debe retornar la suma de la cantidad de veces que aparecen cada uno de los caracteres en la cadena.

Hint: No utilizar la función .count() de las cadenas. Cada vez que la invocamos, Python realiza un recorrido por la cadena buscando la subcadena que la función recibe como parámetro. Resolver el ejercicio realizando una única iteración en toda la cadena.

Ejemplo:

    contar_caracteres("casa", "c", "a") => 3
    contar_caracteres("cosa", "c", "a") => 2
    contar_caracteres("algoritmos", "a", "o") => 3
    contar_caracteres("algoritmos", "w", "x") => 0"""


def contar_caracteres(cadena,caracter1,caracter2):

    letras = ""

    for i in cadena:

        if caracter1 in i:



            letras+=i

        elif caracter2 in i:
            letras+=i    

    return len(letras)

print(contar_caracteres("casa", "c", "a"))
print(contar_caracteres("cosa", "c", "a"))
print(contar_caracteres("algoritmos", "a", "o"))
print(contar_caracteres("algoritmos", "w", "x"))


"""Completar el cuerpo de la función. La misma debe retornar un valor booleano: True en caso de que las palabra que se recibe sea capicúa, False en caso contrario.

Intentar resolver el ejercicio en una línea.

Ejemplos:

    es_capicua("neuquen") => True
    es_capicua("mendoza") => False
    es_capicua("menem") => True
    es_capicua("alfonsin") => False"""

def es_capicua(nombre):

    if str(nombre) == str(nombre)[::-1]:

        return True
    
    else:
        return False
    
print(es_capicua("neuquen"))
print(es_capicua("mendoza")) 
print(es_capicua("menem") ) 
print(es_capicua("alfonsin")) 

"""Completar el cuerpo de la función. La misma recibe una cadena y debe retornar la misma habiendo filtrado todas las vocales que contenía.

Ejemplos:

    filtrador_de_vocales("hola") => "hl"
    filtrador_de_vocales("facultad") => "fcltd"
    filtrador_de_vocales("algoritmos") => "lgrtms"""

def filtrador_de_vocales(palabras):

    vocales = "aeiou"
    letras = ""
    
    for i in palabras:

        if i not in vocales:

            letras+=i

    return letras

print(filtrador_de_vocales("hola"))   
print(filtrador_de_vocales("facultad"))  
print(filtrador_de_vocales("algoritmos")) 

#----------------------------------------FUNCIONES DE LISTA-------------------------------------------------------

"""Completar los cuerpos de las distintas funciones. A continuación se encuentran los requerimientos que deben cumplir cada una de las funciones. Las funciones deben ser resueltas realizando iteraciones sobre las listas, no se pueden usar funciones de ordenamiento.

filtrar_pares: Recibe una lista con variables numéricas enteras. Retorna una nueva lista con todos los números pares que estaban en la lista que se recibió como parámetro. Los elementos de la lista devuelta deben estar en el orden original.

Ejemplo:

    filtrar_pares([5,6,13,7,11,9,10,11]) => [6,10]"""


def filtrar_pares(lista_numeros):

    filtracion = [x for x in lista_numeros if x % 2==0]

    return filtracion


print(filtrar_pares([5,6,13,7,11,9,10,11]))

"""filtrar_primos: Recibe una lista con variables numéricas enteras. Retorna una nueva lista con todos los números primos que estaban en la lista que se recibió como parámetro Los elementos de la lista devuelta deben estar en el orden original.

Hint: Utilizar la función programada en otra actividad que determina si un número es primo o no.

Ejemplo:

    filtrar_primos([5,6,13,7,11,9,10,11]) => [5,13,7,11,11]"""

def es_primo(numero):
   
   contador=0

   for i in range(1,numero+1):
    
    if numero % i == 0:

        contador +=1

   if contador ==2:

    return True

   else:
    return False
   

def filtrar_primos(lista):

    filtracion_lista = []

    for i in lista:

        if es_primo(i):

            filtracion_lista.append(i)

    return filtracion_lista

print(filtrar_primos([5,6,13,7,11,9,10,11])) 

"""sumar_elementos: Recibe una lista con variables numéricas. Retorna la suma de todos sus elementos.
No se puede utilizar la función sum(), ya existente en Python.

Ejemplo:

    sumar_elementos([5,6,13,7,11,9,10,11]) => 72"""

def sumar_elementos(lista):

    suma = 0
    contador = 0

    for i in lista:

        suma+=i
        contador+=1

    return suma

print(sumar_elementos([5,6,13,7,11,9,10,11]))    


"""esta_ordenada: Recibe una lista con variables numericas. Retorna True en caso de que la lista este ordenada ascendentemente (es decir, los mas chicos en las primeras posiciones), False en caso contrario.

Ejemplos:

    esta_ordenada([5,6,13,7,11,9,10,11]) => False
    esta_ordenada([5,6,7,11]) => True"""

def esta_ordenada(lista):

    return lista == sorted(lista)

print(esta_ordenada([5,6,13,7,11,9,10,11]))
print(esta_ordenada([5,6,7,11]))


"""producto_escalar: Recibe dos listas de variables numéricas con la misma longitud. Interpretarlas como vectores. Retorna el producto escalar entre ambos vectores.

Ejemplos:

    producto_escalar([2,5,3], [4,6,7]) => 59"""

def producto_escalar(lista1,lista2):

    resultado = 0

    for i in range(len(lista1)):

        resultado+=lista1[i]*lista2[i]

    return resultado    

print(producto_escalar([2,5,3], [4,6,7]))  


"""letras_en_palabras: Recibe una lista de letras y una cadena. La lista contiene en cada índice de la misma una letra (string de longitud 1). Retorna True en caso de que todas las letras se encuentren en la palabra, False en caso contrario.

Ejemplos:

    letras_en_palabras(["a","h","e"], "hola como estas") => True
    letras_en_palabras(["a","h","e"], "ola como estas") => False"""

def letras_en_palabras(letras, frase):
    
    for i in letras:
        if i not in frase:
            
            return False
        
    return True

print(letras_en_palabras(["a","h","e"], "hola como estas"))
print(letras_en_palabras(["a","h","e"], "ola como estas"))







    


