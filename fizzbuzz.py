# Escribir un programa en python que de solución al problema del FizzBuzz: 
# Imprimir en pantalla los número del 1 al 100 pero cambiando los números 
# que sean múltiplos de 3 por la palabra "Fizz", los que sean múltiplos de 5
# por la palabra "Buzz" y los que sean múltiplos de ambos poner la palabra “FizzBuzz”

def fizzbuzz(numero:int) -> str:
    '''Retorna la cadena asociada al número introducido
    dependiendo si es múltiplo de 3, 5, ambos o ninguno'''
    if numero % 3 == 0 and numero % 5 == 0: return 'FizzBuzz'
    if numero % 3 == 0: return 'Fizz'
    if numero % 5 == 0: return 'Buzz'
    return numero

# PROBANDO FIZZBUZZ
for numero in range(1, 101):
    print(fizzbuzz(numero))
