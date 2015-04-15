import math
primes = 2

def primeCheck(x):
    for n in range(2,int(math.sqrt(x)+1)):
        if x%n == 0:
            return False
            break
    else:
        return True

for n in range(3,2000000):
    if primeCheck(n) == True:
        primes += n
print primes
