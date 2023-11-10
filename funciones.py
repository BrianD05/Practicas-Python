"""Ejercicio 1: Declaración y Llamada a Funciones
Crea una función llamada saludar que imprima "¡Hola, mundo!".
Llama a la función saludar."""

def saludar():

    print("¡Hola, mundo!")

saludar()

"""Ejercicio 2: Parámetros y Argumentos
Crea una función llamada sumar que tome dos parámetros (a y b) y devuelva la suma de ambos.
Llama a la función sumar con dos números e imprime el resultado."""

def sumar(a,b):

    suma = a + b

    return suma

suma_numeros = sumar(5,6)

print(suma_numeros)


"""Ejercicio 3: Funciones con Valor por Defecto
Modifica la función sumar para que tenga un valor por defecto de 0 para el parámetro b.
Llama a la función sumar solo con un argumento e imprime el resultado."""

def sumar(a,b = 0):

    sumar = a + b

    return sumar

print(sumar(5))

"""Ejercicio 4: Funciones Lambda
Crea una función lambda que multiplique dos números.
Llama a la función lambda con dos números e imprime el resultado."""


funcion_lambda = lambda x,y:x*y
resultado = funcion_lambda(4,7)

print(resultado)

"""Ejercicio 5: Funciones con Retorno de Valores
Crea una función llamada elevar_al_cuadrado que tome un número como parámetro y devuelva su cuadrado.
Llama a la función elevar_al_cuadrado con un número e imprime el resultado."""

def elevar_al_cuadrado(numero):

    return numero**2

resultado2 = elevar_al_cuadrado(5)

print(resultado2)

"""Ejercicio 6: Funciones con Listas
Crea una función llamada duplicar_lista que tome una lista como parámetro y devuelva una nueva lista con cada elemento duplicado.
Llama a la función duplicar_lista con una lista e imprime el resultado."""

def duplicar_lista(lista):

    return [elemento*2 for elemento in lista]

lista1 = [1,2,4,5,3,2,5,2,5]
resultado3 = duplicar_lista(lista1)

print(resultado3)

"""Ejercicio 7: Funciones Recursivas
Crea una función recursiva llamada factorial que calcule el factorial de un número.
Llama a la función factorial con un número e imprime el resultado."""

def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n-1)

resultado = factorial(5)
print(resultado)

"""Ejercicio 8: Funciones con Argumentos Arbitrarios
Crea una función llamada concatenar que acepte cualquier número de argumentos de tipo cadena y devuelva la concatenación de todos ellos.
Llama a la función concatenar con al menos tres cadenas e imprime el resultado."""


def concatenar(*palabras):
    return ''.join(palabras)

resultado = concatenar("Hola", ", ", "mundo")
print(resultado)





