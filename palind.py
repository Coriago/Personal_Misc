x = str(4234)
xl = []
palindtaf = []
palindfinals = []
qq = 999
def palindCheck():
    for digit in x:
        xl.append(digit)
    for iteration in range(len(xl)):
        if xl[iteration] == xl[(len(xl)-1)-iteration]:
            palindtaf.append(True)
        else:
            palindtaf.append(False)
    if palindtaf.count(False) == 0:
        palindfinals.append(int(x))
for qq in range(1,999,1):
    for q in range(1,999,1):
        x = q * qq
        x = str(x)
        xl = []
        palindCheck()
        palindtaf = []
palindfinals.sort()
print palindfinals
