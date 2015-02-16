import math
a = 0
b = 0
while b < 500:
    while a < 500:
        c = a**2 + b**2
        if a + b + math.sqrt(c) == 1000:
            print str(a) +" "+ str(b) +" "+ str(math.sqrt(c))
            print a * b * math.sqrt(c)
        a += 1
    b += 1
    a = 0
