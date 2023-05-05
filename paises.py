#le pido al usuario que me envie la lista de paises

lista_paises = input("Introduce países separados por comas: ")

#convieto el input a una lista y le quito los espacios
paises = [pais.strip() for pais in lista_paises.split(",")]

#evito los paises repetidos
paises_no_repetidos = set(paises)

#los ordeno y creo una lista
paises_ordenados = sorted(list(paises_no_repetidos))
#muestro en la consola la lista de paises ordenados y separados por coma
print(f'la lista ordenada es {paises_ordenados}')
