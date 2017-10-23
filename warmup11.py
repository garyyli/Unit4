#Gary Li
#10/23/17
#warmup11.py - determine if a number is prime

def isPrime(n):
    for i in range(2,n):
        if n%i == 0:
            return False
        return True
    else:
        return True

print(isPrime(20))
