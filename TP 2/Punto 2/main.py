from juego import jugar_partida, limpiar_pantalla

OPCION_UNO = "1"
OPCION_DOS = "2"
RESPUESTA_SI = 's'

def main():
    nombre = input("Ingrese su nombre: ").lower()
    puntos_totales = 0

    opcion = OPCION_UNO  

    while opcion != OPCION_DOS:  
        limpiar_pantalla()
        print(f"Hola, {nombre} Bienvenido al juego del Ahorcado!")
        print("Menú:")
        print(f"{OPCION_UNO}. Jugar")
        print(f"{OPCION_DOS}. Salir")

        opcion = input("Seleccione una opción: ")
        limpiar_pantalla()

        if opcion == OPCION_UNO:
            puntos_partida = jugar_partida()
            puntos_totales += puntos_partida
            print(f"\nPuntos acumulados en esta partida: {puntos_partida}")
            print(f"\nPuntos totales acumulados: {puntos_totales}")

            respuesta = input("\n¿Desea jugar otra partida? (s/n): ").lower()
            if respuesta != RESPUESTA_SI:
                opcion = OPCION_DOS  

        elif opcion == OPCION_DOS:
            print(f"Gracias por jugar, {nombre}.")
            print(f"Puntos totales en esta partida: {puntos_totales}")

        else:
            print("Opción no válida. Por favor, seleccione 1 o 2.")

    limpiar_pantalla()
    print(f"Gracias por jugar, {nombre}.")
    print(f"Puntos totales acumulados en todas las partidas: {puntos_totales}")

if __name__ == "__main__":
    main()
