#Get num
import math
bigNum = 600851475143

def primeCheck(x):
    for n in range(2,int(math.sqrt(x))):
        if x%n == 0:
            return False
            break
    else:
        return True
        


#divide by incremeants
for n in range(2,100000000):
#if factor found check large num for prime if not
    if bigNum%n == 0:
        check = bigNum/n
        if primeCheck(check) == True:
            print bigNum/n
            break
        else:
            print "Not prime"
            pass
print "No values in the range found"
#Continue incremeanting
