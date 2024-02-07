from string import punctuation
import doctest

LONGITUD_MIN = 8

LONGITUD_MAX = 12

VOCALES = 'ÁÉÍÓÚáéíóú'

def validar(clave):
    
    """
    Funcion que valida caracteres segun ciertas restricciones.

    >>> validar("Algoritmo $1")
    False
    >>> validar("Aprobé-con-7")
    False
    >>> validar("Algoritmo$1")
    True
    >>> validar("Aprobe-con-7")
    True
    >>> validar("Valid@123")
    True
    >>> validar("SinSimboloS")
    False
    
    """
    
    CONTIENE_MAYUSCULA = False

    CONTIENE_MINUSCULA = False

    CONTIENE_NUMERO = False

    TIENE_PUNTUACION = False

    SIN_ESPACIO = True

    SIN_TILDES = True

    longitud = len(clave)

    i = 0
    
    while i < longitud:
        caracter = clave[i]

        if caracter.isdigit():
            CONTIENE_NUMERO = True

        elif caracter.isupper():
            CONTIENE_MAYUSCULA = True

        elif caracter in punctuation:
            TIENE_PUNTUACION = True

        elif caracter.isspace():
            SIN_ESPACIO = False

        elif caracter in VOCALES:
            SIN_TILDES = False

        elif caracter.islower():
            CONTIENE_MINUSCULA = True

        i+= 1

    return (LONGITUD_MIN <= longitud <= LONGITUD_MAX and CONTIENE_NUMERO and CONTIENE_MAYUSCULA and CONTIENE_MINUSCULA and TIENE_PUNTUACION and SIN_ESPACIO and SIN_TILDES)


print(doctest.testmod())                          
