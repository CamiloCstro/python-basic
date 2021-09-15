calificacion = 5
color = None

if calificacion >= 7:
    color = 'Verde'
else:
    color = 'Rojo'

print(calificacion, color)


color = 'verde' if calificacion >= 7 else 'rojo'
print(calificacion, color)