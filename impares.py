from functools import reduce

#creo una lista
lista = [1, 2, 4, 7, 6, 9, 11, 3]

#busco los impares dentro de la lista
impares = filter(lambda x: x % 2 != 0 , lista)

#sumo cada uno de los impares
suma_impares = reduce(lambda x, y : x + y, impares)

print(f'la suma es : {suma_impares}')