def procesar_votaciones(votaciones):
    """
    PRE: La funcion espera una lista de votaciones valida y no vacia.
    
    POST: Devuelve un diccionario que resume la sumatoria, cantidad y promedio de puntajes para cada participante, asegurando los datos.

    """
    CONTADOR_PUNTAJES = 1
    RESULTADOS_PARTICIPANTES = {}
    
    for votacion in votaciones:
        nombre_participante = votacion[0]
        puntaje_participante = votacion[1]
        
        if nombre_participante not in RESULTADOS_PARTICIPANTES:
            RESULTADOS_PARTICIPANTES[nombre_participante] = [puntaje_participante, CONTADOR_PUNTAJES]
        else:
            RESULTADOS_PARTICIPANTES[nombre_participante][0] += puntaje_participante
            RESULTADOS_PARTICIPANTES[nombre_participante][1] += CONTADOR_PUNTAJES
    
    for nombre_participante, datos in RESULTADOS_PARTICIPANTES.items():
        sumatoria_puntaje = datos[0]
        cantidad_puntajes = datos[1]
        promedio_puntaje = sumatoria_puntaje / cantidad_puntajes
        RESULTADOS_PARTICIPANTES[nombre_participante] = [sumatoria_puntaje, cantidad_puntajes, promedio_puntaje]
    
    return RESULTADOS_PARTICIPANTES


def mostrar_resultados_participantes(resultados_participantes):
    
    """
    Muestra los resultados de los participantes ordenados de mayor a menor por promedio de puntaje

    """
    resultados_participantes_ordenados = sorted(resultados_participantes.items(), key=lambda x: x[1][2], reverse=True)
    
    for nombre_participante, datos in resultados_participantes_ordenados:
        promedio_puntaje = datos[2]
        print(f"{nombre_participante}: {promedio_puntaje} ")


def main():
    votaciones = [["Luisa", 4], ["Mariano", 10], ["Luisa", 5]] 
    resultados_participantes = procesar_votaciones(votaciones)
    mostrar_resultados_participantes(resultados_participantes)


if __name__ == "__main__":
    main()