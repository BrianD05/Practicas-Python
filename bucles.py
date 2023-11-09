"""Bucles (for, while):

Escribe un programa que imprima los números del 1 al 10 utilizando un bucle for.

Desarrolla un programa que calcule la suma de los números enteros del 1 al 100 utilizando un bucle while.

Crea un programa que solicite al usuario un número y luego imprima los primeros "n" números pares utilizando un bucle for.

Desarrolla un programa que muestre la tabla de multiplicar de un número ingresado por el usuario del 1 al 10 utilizando un bucle while."""

#Escribe un programa que imprima los números del 1 al 10 utilizando un bucle for.

for i in range(1,11):

    print(i)

#Desarrolla un programa que calcule la suma de los números enteros del 1 al 100 utilizando un bucle while.

suma = 0
contador = 0

while contador <=100:

    suma+=contador
    contador+=1

print(suma)

#Crea un programa que solicite al usuario un número y luego imprima los primeros "n" números pares utilizando un bucle for.

ingresar_numero = int(input("Ingrese Numero: "))

for i in range(1,ingresar_numero + 1):

    if i %2==0:
        print(i)

#Desarrolla un programa que muestre la tabla de multiplicar de un número ingresado por el usuario del 1 al 10 utilizando un bucle while.

ingresar_numero2= int(input("Ingrese numero para la tabla de multiplicar: "))
contador = 1

while contador <=10:

    print(f"{ingresar_numero2} X {contador} = {ingresar_numero2*contador} ")
    contador+=1

        

