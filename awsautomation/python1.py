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
'''
class Netflix():
    def __init__(self, nome, plano, email):
        self.nome = nome
        self.plano = plano
        self.email = email
        self.lista_planos = ["basic", "premium"]
        if plano in self.lista_planos:
            self.plano = plano
        else:
            raise Exception ('Plano inválido')
    def mudar_de_plano(self,mudar):
        if mudar in self.lista_planos:
            self.plano = mudar
        else:
            print('Plano inválido')
    def ver_filme(self, filme, plano_filme):
        if self.plano == plano_filme:
            print(f"Pode ver o filme {filme}")
        elif self.plano == 'premium':
            print(f"Pode ver o filme {filme}")
        elif plano_filme == 'premium' and self.plano == 'basic':
            print('Faço um upgrade do seu plano')
        else:
            raise Exception ('Error 404')
            
x = Netflix('Joao', 'basic', 'gmail')

x.ver_filme('harry potter', 'premium')
'''

import math
x = float(input('Digite sua altura em cm:'))
a = x / 100
y = float(input('Digite seu peso em kg:'))
b = y / a**2

if b < 18.5:
    print('Magreza')
elif 18.5 <= b <= 24.9:
    print('Normal')
elif 25.0 <= b <= 29.9:
    print('Sobrepeso')
elif 30.0 <= b <= 39.9:
    print('Obesidade')
elif b >=40:
    print('Obesidade grave')



























