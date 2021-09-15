# serch strings in to other string

tittle_curse = 'python curse curse'

# Cuenta el numero de veces que aparece una secuencia de caracteres en un string
print(tittle_curse.count('curse'))

# Retorna true o false
# si la palabra 'python' se encuentra incluida en la variable tittle_curse
print('python' in tittle_curse)

# Retorna true o false
# si una secuencia de caracteres comienza con el string o caracter indicado
print(tittle_curse.startswith('python3'))

'''.endsWith() Retorna true o false si el string se encuentra al final de la variable'''
print(tittle_curse.endswith('curse'))

'''.upper() cambia el string a mayuscula .lowe() cambia el string a minuscula'''
print(tittle_curse.upper())
print(tittle_curse.lower())
