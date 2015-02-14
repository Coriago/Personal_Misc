countOf3 = 0
countOf5 = 0
accumOf3 = 0
accumOf5 = 0
while countOf3 <= 1000
    countOf3 += 3
    accumOf3 += countOf3
while countOf5 <= 1000
    countOf5 += 5
    accumOf5 += countOf5
print accumOf3 + accumOf5
