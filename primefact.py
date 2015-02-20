whol = 930481
div = 2
primefs = [1]
ind = 0
fakedivs = []
while max(primefs) < (whol / max(primefs)):
    if whol % div == 0:
        primefs.append(div)
        print str(whol) + " is divisible by " + str(div)
    for number in primefs:
        if primefs.count(number) > 1:
            primefs.remove(number)
    div += 1
primefs.remove(1)
for n in primefs:
    for m in primefs:
        if (n % m == 0) and (n != m):
            fakedivs.append(n)
for q in fakedivs:
    if fakedivs.count(q) > 1:
        fakedivs.remove(q)
for fakes in fakedivs:
    primefs.remove(fakes)
print "prime factors of " + str(whol) + " = " + str(primefs)
print "largest prime factor = " + str(max(primefs))
