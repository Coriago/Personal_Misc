import time

def collatz(n):     ##returns a list
    seq = []
    seq.append(n)
    while not 1 in seq:
        if n % 2 == 0:
            seq.append(n/2)
            n /= 2
        if n % 2 != 0:
            seq.append(3*n+1)
            n = 3*n+1
    if seq[len(seq)-1] != 1:
        seq.pop()
    return seq
start = time.time()
acctime = 0
startn = 1
longchain = 0

while startn != 1000000:
    if time.time() > start + 5:
        acctime += 5
        print 1000000 - startn, "to go,", acctime, "seconds total (takes 105 seconds on my pc)" 
        start = time.time()
    if len(collatz(startn)) > longchain:
        print "current longest chain:", startn
        longchain = len(collatz(startn))
    startn += 1

