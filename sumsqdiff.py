sumsqhundred = 0
sumhundred = 0
for n in range(100,0,-1):
    sumsqhundred += (n ** 2)
for m in range(100,0,-1):
    sumhundred += m
sumhundred = sumhundred ** 2
print sumhundred - sumsqhundred
