#10001st prime
import time

candidate = 2
isPrime = True
primes = 0
lastPrime = 0

start = time.time()

while primes <= 10000:      #10001
    isPrime = True
    for n in range(candidate-1,1,-1):
        if candidate % n == 0:
            isPrime = False
##    numBel = candidate - 1
##    while numBel > 1:
##        if candidate % numBel == 0:
##            isPrime = False
##        numBel -= 1
    if isPrime:
        primes += 1
        lastPrime = candidate
    candidate += 1
end = time.time()
print end - start
