''' 
Permiten almacenar diferentes tipos de datos, son inmutables.
No se pueden modificar sus elementos, solo se pueden acceder a ellos.
'''

tupla = ('String', 1, 1.2, True, [3, 4, 5], (7, 8, 9))
print(tupla)

first_element = tupla[0]
print(first_element)

# generar subtuplas
sub_tupla = tupla[:5]
print(sub_tupla)

lista_uno = [1, 2, 3, 4]
tupla_uno = [5, 6, 7, 8]

# Generar tuplas apartir de listas
lista_uno_tupla = tuple(lista_uno)
print(type(lista_uno_tupla))

# Generar listas apartir de tuplas
tupla_uno_lista = list(tupla_uno)
print(type(tupla_uno_lista))
