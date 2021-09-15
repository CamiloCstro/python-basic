# Desempaquetar valores y variables
numeros = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)

# * -> lista
# el * indica que almacene el resto de valores en una nueva variable de tipo lista
uno, dos, tres, cuatro, *mas_valores = numeros
print(numeros)
print(mas_valores)

print('Ejemplo 2')
# Podemos utilizar el *_ para omitir los demas valores
numeros_dos = (1, 2, 3, 4, 5, 6, 7)
uno, dos, tres, cuatro, *_ = numeros_dos
print(uno, dos, tres, cuatro)

print('Ejemplo 3')
numeros_tres = (1, 2, 3, 4, 5)
uno, dos, *resto, cinco = numeros_tres
print(uno, dos, cinco)
print(resto)
print(numeros_tres)

print('Ejemplo 4')
numeros_cuatro = (1, 2, 3, 4)
uno, _, tres, _ = numeros_cuatro
print(uno, tres, numeros_cuatro)
