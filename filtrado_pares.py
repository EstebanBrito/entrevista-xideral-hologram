# Escribe una función para filtrar números pares en una lista

def filtrar_pares(lista:list) -> None:
    '''Dada una lista, imprime en pantalla aquellos valores pares'''
    for numero in lista:
        if numero % 2 == 0:
            print(numero)

def filtrar_pares2(lista:list) -> list:
    pares = filter(lambda x: x % 2 == 0, lista)
    print(list(pares))
    return pares

# PROBANDO FILTRADO
lista_a = [1, 2, 3, 5, 8, 13]
filtrar_pares2(lista_a)