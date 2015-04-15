fibs = []
fibs.append(1)
fibs.append(2)
evenfibs = []
sumofevenfibs = 0
fibdex = 0
while max(fibs) < 4000000:
    fibs.append(fibs[fibdex] + fibs[fibdex + 1])
    fibdex += 1
for n in fibs:
    if n > 4000000:
        fibs.remove(n)
    if n % 2 == 0:
        evenfibs.append(n)
for even in evenfibs:
    sumofevenfibs += even
