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


def distance(a, b, c, d):
    return (sqrt(((d-b)**2)+((c-a)**2)))
    
SideA = distance(x1, x2, y1, y2)
SideB = distance(x2, x3, y2, y3)
SideC = distance(x3, x1, y3, y1)

def semiperimeter