numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

"""Crea una lista que contenga los cuadrados de cada número en numeros.
   Crea una lista que contenga solo los números pares de numeros."""

lista_numero_cuadrado = [x**2 for x in numeros]

print(lista_numero_cuadrado)

lista_numeros_pares = [y for y in numeros if y %2 == 0]
print(lista_numeros_pares)

palabras = ["Python", "es", "divertido", "y", "poderoso"]

"""Crea una lista que contenga las palabras que tienen más de tres letras.
Crea una lista que contenga las palabras convertidas a minúsculas."""

lista_palabras = [x for x in palabras if len(x) > 3]

print(lista_palabras)

lista_palabras2 = [palabra.lower() for palabra in palabras]
print(lista_palabras2)

temperaturas_celsius = [0, 10, 20, 30, 40]

"""Crea una lista que contenga las temperaturas convertidas a grados Fahrenheit utilizando la fórmula: F = (C * 9/5) + 32."""

temperaturas_fahrenheit = [(c * 9/5) + 32 for c in temperaturas_celsius]

print(temperaturas_fahrenheit)

numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

"""Crea una lista que contenga "Par" si el número es par y "Impar" si el número es impar."""

numeros_pares_impares = ["Par" if x % 2==0 else "Impar" for x in numeros]

print(numeros_pares_impares)