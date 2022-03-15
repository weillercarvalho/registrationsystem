'''
import os
import random 
x = random.randint(1, 1000)
if x > 1:
    x = {'a'}
    y = open(x, 'w')
    y.write('Te amo gordinha')
    y.close()
    y = open(x, 'r')
    print(y.read())
    y.close()

else:
    print()

if os.path.exists('Nicole.txt'):
    os.remove('Nicole.txt')
else:
    print()
'''

def x(a):
    return lambda n: n + a
y = x(2)

print(y(4))
