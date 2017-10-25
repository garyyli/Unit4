#Gary Li
#10/25/17
#triangle.py

from math import sqrt

x1 = int(input('Enter x1: '))
y1 = int(input('Enter y1: '))
x2 = int(input('Enter x2: '))
y2 = int(input('Enter y2: '))
x3 = int(input('Enter x3: '))
y3 = int(input('Enter y3: '))


def distance12(x1, x2, y1, y2):
    return (sqrt(((y2-y1)**2)+((x2-x1)**2)))

def distance23(x2, x3, y2, y3):
    return (sqrt(((y3-y2)**2)+((x3-x2)**2)))

def distance31(x3, x1, y3, y1):
    return (sqrt(((y1-y3)**2)+((x1-x3)**2)))
