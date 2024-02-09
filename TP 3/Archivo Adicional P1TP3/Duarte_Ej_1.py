"""p = [5, 3, 8, 9, 7]
def calc(a, b, c):
if (c == 0):
 return -1
 elif (a[c] == b):
return c
else:
 calc(a, b, c - 1)
x = input()
calc(p, x, length(p))"""

"""p = [5, 3, 8, 9, 7]
def calc(a, b, c):
    if c == 0:
        return -1
    elif a[c-1] == b:  # Corrijo el indice para evitar IndexError
        return c-1
    else:
        return calc(a, b, c - 1)  # Agrego "return" para mantener y retornar el resultado de la llamada recursiva.


x = int(input(""))  # Convierto la entrada a entero "int"
result = calc(p, x, len(p))  # Se corrige el error tipografico y se nombra "len(p)"
print(result)"""

#Codigo mas legible y mas autentico 

def buscar_indice_elemento(lista, elemento, indice):
    
    """
    PRE: La lista debe tener al menos un elemento, y el Indice y el elemento buscado deben ser validos.

    POST: La función devuelve un Indice valido (o -1 si el elemento no se encuentra), buscando el elemento de manera descendente en la lista.
    
    """
    if indice == 0:
        return -1
    elif lista[indice - 1] == elemento:
        return indice - 1
    else:
        return buscar_indice_elemento(lista, elemento, indice - 1)

def main():
    lista_numeros = [5, 3, 8, 9, 7]  
    numero_buscado = int(input("Ingrese un número: "))  
    resultado = buscar_indice_elemento(lista_numeros, numero_buscado, len(lista_numeros))
    if resultado != -1:
        print(f"El elemento {numero_buscado} se encuentra en el Indice {resultado}.")
    else:
        print(f"El elemento {numero_buscado} no se encuentra en la lista.")

if __name__ == "__main__":
    main()

