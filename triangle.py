#Gary Li
#10/25/17
#triangle.py

from math import sqrt

x1 = int(input('Enter x1: '))
y1 = int(input('Enter y1: '))
x2 = int(input('Enter x1: '))
y2 = int(input('Enter y2: '))
x3 = int(input('Enter x1: '))
y3 = int(input('Enter y3: '))


def distance(x1, x2, y1, y2):
    return (sqrt(((y2-y1)**2)+((x2-x1)**2)))

print(distance(2,2,2,4))

def semiperimeter