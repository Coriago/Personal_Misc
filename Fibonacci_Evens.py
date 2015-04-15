secondNum = 1
firstNum = 0
newNum = 0
total = 0
while secondNum < 4000000:
    newNum = secondNum + firstNum
    firstNum = secondNum
    secondNum = newNum
    print newNum
