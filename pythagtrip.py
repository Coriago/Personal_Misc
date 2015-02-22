def isPythagorean(a,b,c):
    if a < b and b < c and (a**2 + b**2 == c**2):
        return True
    else:
        return False
    
for a in range(500):
    for b in range(500):
        for c in range(500):
            if isPythagorean(a,b,c) and (a + b + c) == 1000:
                print a*b*c
                exit()
