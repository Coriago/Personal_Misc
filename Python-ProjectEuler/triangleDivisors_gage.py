totalDivisors = []
totalTriangles = []
triangleVal = 0
found = False
increasevalue = 10000
divisorAmt = 500

def factorAdder(x):
    divisors = 0
    for i in range(x):
        if x%(i+1) == 0:
            divisors += 1
    totalDivisors.append(divisors)

print "Initiating..."
for i in range(increasevalue):
    triangleVal += i
    totalTriangles.append(triangleVal)
    factorAdder(triangleVal)
    if totalDivisors[i] > divisorAmt:
        print "The triangle value that has over 500 divisors is: " + str(totalTriangles[i])
        found = True
        break
if found == False:
    print "No values found"

