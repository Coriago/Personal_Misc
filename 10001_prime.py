import math
primes = []

def primeCheck(x):
    for n in range(2,int(math.sqrt(x)+1)):
        if x%n == 0:
            return False
            break
    else:
        return True

for i in range(2,1000000):
    if primeCheck(i) == True:
        primes.append(i)
print primes[10000]
