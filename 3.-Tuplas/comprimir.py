lst = [1, 2, 3, 4]
tpl = ('David', 'Axl', 'Bako', 'Shaggi')
names = ['Human', 'Cat', 'Cat', 'Dog']

# objeto de tipo zip
tuple_1 = tuple(zip(tpl, lst, names))
print(tuple_1)
print(tuple_1[0])
print(list(tuple_1))
