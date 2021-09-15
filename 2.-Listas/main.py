''' 
Listas estructura de datos que permite almacenar varios datos
dinamica se pueden agregar o remover elementos
list(), [] utilizar cualquierda de las dos formas
Definir listas de un solo tipo como recomendacion
'''
#          -5         -4     -3     -2      -1
lista = ['Camilo', 'Castro', '24', '1.78', 'True']
#           0          1      2      3       4

# Actualizar elementos haciendo uso de un indice
lista[-1] = 'False'
print(lista)

# Generar sublistas [start:end]
print(lista[0:2])
print(lista[-1])
print(lista[-5])
print(lista)
print(lista[::3])

# Modificar listas

# metodo append agregar un elemento al final de la lista
lista.append('Bogota')
lista.append('Colombia')
print(lista)
print(len(lista))  # longitud de la lista

# Metodo insert agrega un elemento en un indice especifico
lista.insert(0, 'Ing')
print(lista)
lista.insert(1, 'Poli')
print(lista)

# Metodo extend .extend()  añadir los elementos de una lista a otra lista
lista_dos = ['Rojo', 'Uva', 'Santa Fe']
lista.extend(lista_dos)
print(lista)
lista_dos.extend(lista)
print(lista_dos)

# Metodo .remove() elemento a remover en la lista
lista.remove('Uva')
print(lista)

# del elimina un elemento por indice en este caso
# elimina el ultimo elemento de la lista y el primer elemento de la lista
del lista[-1], lista[0]
print(lista)

# Metodo .clear() elimina todos los elementos almacenados de una lista
lista.clear()
print(lista)

# Ordenar una lista .sort()
num_list = [6, 1, 7, 10112, 2, 141291, 11212]
print(num_list)

# Ordenar de menor a mayor
num_list.sort()
print(num_list)

# Ordenar de mayor a menor
num_list.sort(reverse=True)
print(num_list)

# Funcion min y max permite conocer el menor y mayor elemento de una lista
print(min(num_list))
print(max(num_list))

# Conocer si un elemento esta en una lista o no
# palabra reservada in saber si existe un valor en la lista

# 10 no esta en la lista?
print(10 not in num_list)

# 10 esta en la lista?
print(10 in num_list)

# Retorna el indice de un elemento .index(), imprime el indice del primer elemento encontrado
print(num_list.index(141291))
