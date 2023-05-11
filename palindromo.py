# Escribir un programa en python que permita saber si una palabra es palíndromo

def es_palindromo(palabra:str) -> bool:
    '''Determina si una palabra es un palíndromo'''
    # Palabras vacías no son palíndromos
    if len(palabra) == 0: return False
    # Preprocesar palabra (mayúsculas y minúsculas no deben influir si una palabra es un palindromo)
    palabra = palabra.lower()
    # Se recorre la palabra desde ambos extremos para comprobar si es palindromo.
    indice_mitad = len(palabra) // 2
    for indice_actual in range(indice_mitad):
        indice_reflejo = -(indice_actual + 1)
        if palabra[indice_actual] != palabra[indice_reflejo]:
            return False
    return True
    

# PROBANDO FUNCIÓN
print('"" es palíndromo:', es_palindromo('')) # Debe ser False
print('"a" es palíndromo:', es_palindromo('a')) # Debe ser True
print('"Luis" es palíndromo:', es_palindromo('Luis')) # Debe ser False
print('"Ana" es palíndromo:', es_palindromo('Ana')) # Debe ser True