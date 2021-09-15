# Siempre retorna un String por default
name = input('ingresa tu nombre completo: ')
print(name)
age = int(input('ingresa tu edad: '))
print(age)
height = float(input('ingresa tu altura: '))
print(height)
autor = input('Autorizas al programa? (si/no) ')
autor = autor == 'si'
print(autor)

print(type(name))
print(type(age))
print(type(height))
print(type(autor))
