# Nos permiten almacenar diferentes tipos de datos y son mutables
# No se rigen por un indice si no a una llave y un valor.

elements = {1: "Camilo", 2: 'Andres'}
elements_two = {}
elements[(1, 2, 3, 4, 5)] = 'Numeros'
elements[(1, 2, 3, 4, 5)] = 'nums'
print(elements_two)
print(elements)
