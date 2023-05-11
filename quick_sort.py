def intercambiar_valores(lista:list, indice_a:int, indice_b:int) -> None:
    '''Cambia de posición dos valores de una lista'''
    temp = lista[indice_a]
    lista[indice_a] = lista[indice_b]
    lista[indice_b] = temp

def particionar(lista:list, indice_inicio:int, indice_final:int) -> int:
    '''Coloca los valores de la lista más pequeños que cierto
    valor pivote a la izquierda de la misma, y los mayores a
    la derecha. Retorna el índice que separa ambas partes.'''
    # El último valor suele tomarse como valor pivote
    valor_pivote = lista[indice_final]
    # Itera la lista reubicando valores a la izquierda
    indice_separacion = indice_inicio
    for indice_actual in range(indice_inicio, indice_final):
        if lista[indice_actual] < valor_pivote:
            intercambiar_valores(lista, indice_actual, indice_separacion)
            indice_separacion += 1
    # Reubica el valor pivote también
    intercambiar_valores(lista, indice_final, indice_separacion)
    return indice_separacion

def quick_sort(lista:list, indice_inicio:int, indice_final:int) -> None:
    '''Functión que, aplicada recursivamente, realiza un
    ordenamiento de tipo QuickSort en la lista especificada.'''
    # Mientras las particiones sean mayores a 1 elemento, parte
    # la lista en dos y aplica quick sort a ambas partes
    if indice_inicio < indice_final:
        indice_particion = particionar(lista, indice_inicio, indice_final)
        quick_sort(lista, indice_inicio, indice_particion - 1)
        quick_sort(lista, indice_particion, indice_final)


# PROBANDO FUNCIONALIDAD DE QUICK SORT
lista = [34, 7, 15, 9, 29, 1, 87, 45, 17, 10]
print('Lista antes de ordenar:', lista)
quick_sort(lista, 0, len(lista) - 1)
print('Lista después de ordenar:', lista)
