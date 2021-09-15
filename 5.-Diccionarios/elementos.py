# Obeter elementos

diccionario = {'a': 1, 'b': 2, 'c': 3}
valor = diccionario['a']
print(valor)


# saber si una llave existe
print('a' and 'z' in diccionario)


''' retornar un valor con el metodo .get()'''

# si no existe el valor retorna none por default
print(diccionario.get('x'))

# tambien podemos retornar un valor para una llave que nosotros queramos
print(diccionario.get('z', 'No existe la llave en el diccionario'))


'''.setdefault()'''

# si la llave no existe se agrega la llave y se le da un valor por defecto llamado none
print(diccionario.setdefault('f'))

# si la llave no existe se agrega la llave con su respectivo valor al diccionario
print(diccionario.setdefault('e', 3))

# Retorna el valor de una llave
print(diccionario.setdefault('a'))

print(diccionario)
