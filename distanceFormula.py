#Gary Li
#10/20/17
#distanceFormula

from math import sqrt

def distance(x1, x2, y1, y2):
    return (sqrt(((y2-y1)**2)+((x2-x1)**2)))

print(distance(2,2,2,4))
