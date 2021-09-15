
frutas = {'Naranja': 'Amarilla', 'Banano': 'Amarillo',
          'Uva': 'Morado', 'Sandia': 'Rojo'}
print(frutas)

# Elimina apartir de una llave
del frutas['Banano']
print(frutas)

# pop .pop() argumento llave, elimina 'Sandia' en este caso
frutas.pop('Sandia')
print(frutas)

'''Asegurar que el elemento exista para evitar un key error'''
# frutas.pop('Mandarina')
# KeyError: 'Mandarina'

# Eliminar todos los elemenos
frutas.clear()
print(frutas)
