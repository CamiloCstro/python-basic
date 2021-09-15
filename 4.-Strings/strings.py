# Metodos mas utilizados con strings

sentence = 'Java#is#funny!'
# default por espacios
new_sentence = sentence.split('#')
print(new_sentence)

# Metodo join -> permite unir los elementos de un listado apartir de un string
names = ['Camilo', 'Andres', 'Castro', 'Mesa']
result_names = ' '.join(names)
print(result_names)
