#Gary Li
#10/18/17
#returnDemo.py - how to use return with a function

from random import randint

def randevenint(low,high):
    num = rnadint(low,high)
    while num%2 == 1: #while the number is odd
        num = rnadint(low,high)
    return num
    
r1 = randevenint(1,100)
r2 = randevenint(1,100)
r3 = randevenint(1,100)
print(r1, r2, r3)