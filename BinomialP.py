import math
while True:
    try: 
        total = int(input("Enter the total amount of the series: "))
        probability = float(input("Enter the probability: "))
        amountCorrect = int(input("Enter the amount of correct outcomes: "))
        possibles = math.factorial(total)/(math.factorial(amountCorrect)*math.factorial(total-amountCorrect))
    
        print possibles*((probability)**amountCorrect)*((1-(probability))**(total-(amountCorrect)))
    except NameError, SyntaxError:
        print "Enter numerical values"
