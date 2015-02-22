##import time
##start = time.time()
##start2 = time.time()
##def primemark(q):  
##    for num in range(q,(whol / q) + 1):
##        cand[num*q] = "marked"
##def rtnp(z):
##    for e in range(z+1, whol+1):
##        if cand[e] != 'marked':
##            return e
##    else:
##        return False
##whol = 100000
##cand = {x: "not marked" for x in range(2,whol + 1)}
##p = 2
##sumofprimesbelowtwomil = 0
##while 'not marked' in cand.values()[p:len(cand)-1]:
##    if time.time() > start2 + 2:
##        print p
##        start2 = time.time()
##    primemark(p)
##    if rtnp(p) == False:
##        break
##    p = rtnp(p)
##    
##for kl in cand:
##    if cand[kl] == "not marked":
##        sumofprimesbelowtwomil += kl
##else:
##    print whol
##    print str(time.time() - start) + " seconds"
##    print ((1.2428571*(10**-9)*whol**2)+(1.7117143*(10**-4)*whol)+-2.96)
##    print 2000000 / whol
#not efficient enough... :s

##mostly not original code below:
primesum = 0
marked = set()
for z in range(2, 2000001):     #
    if z not in marked:
        primesum += z
        marked.update(range(z**2,2000001,z))
else:
    print primesum

