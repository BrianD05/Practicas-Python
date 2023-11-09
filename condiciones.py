"""Condicionales (if, else, elif):

Escribe un programa que determine si un número ingresado por el usuario es positivo, negativo o cero.

Crea un programa que pida al usuario su edad y determine si es un niño (menos de 12 años), adolescente (entre 12 y 18 años), adulto (entre 19 y 60 años) o adulto mayor (más de 60 años).

Desarrolla un programa que solicite al usuario un número entero y verifique si es par o impar.

Crea un programa que determine si un año ingresado por el usuario es bisiesto. Un año es bisiesto si es divisible por 4, excepto los años que son divisibles por 100 pero no por 400."""

ingresar_numero = int(input("Ingrese un numero: "))

if ingresar_numero < 0:

    print("Negativo")

elif ingresar_numero > 0:

    print("Positivo") 

else:
    print("CERO")

#Crea un programa que pida al usuario su edad y determine si es un niño (menos de 12 años), adolescente (entre 12 y 18 años), adulto (entre 19 y 60 años) o adulto mayor (más de 60 años).

ingresar_edad = int(input("Ingrese su edad: "))

if ingresar_edad < 12:

    print("Sos un Niño")

elif ingresar_edad <= 12 and ingresar_edad <= 18:

    print("Adolescente")

elif ingresar_edad >=19 and ingresar_edad <= 60:
    print("Adulto") 


else:
    print("Adulto Mayor")       


#Desarrolla un programa que solicite al usuario un número entero y verifique si es par o impar.

ingresar_numero2 = int(input("Ingrese un Numero: "))


if ingresar_numero2 %2==0:

    print("Es par")

else:
    print("Es impar")    

año = int(input("Ingrese un año: "))

if año % 4 == 0:
    if año % 100 != 0 or año % 400 == 0:
        print("El año {} es bisiesto.".format(año))
    else:
        print("El año {} no es bisiesto.".format(año))
else:
    print("El año {} no es bisiesto.".format(año))
