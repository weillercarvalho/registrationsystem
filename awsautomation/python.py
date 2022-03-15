'''
lista = ['Weiller', 'Nicole', 'Maria', 'Blue']

lista2 = [a for a in lista if 'e' in a]

print(lista2)

'''
'''
lista = ['Weiller', 'Nicole', 'Maria', 'Blue']

list2 = []

for a in lista:
    if 'e' in a:
       list2.append(a)
print(list2)
'''
'''
from sys import getsizeof

valores = [x * 10 for x in range(100)]
print(valores)
print(getsizeof(valores))

print('===')

valores2 = (x * 10 for x in range(100)) (Generator Expressions/Genex)
print(list(valores2))
print(getsizeof(valores2))
'''