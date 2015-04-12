try:
    while True:
        try:
            #Get values for variables
            startAmount = input("Enter starting amount: ")
            rate = input("Enter rate: ")
            time = input("Enter interval time: ")
            compundAmt = input("How many times to compund: ")
            #Calculate rates with for loop
            print " Start amount: " + str(startAmount) + "\n Rate: " + str(rate) + "\n Time: " + str(time) 
            for n in range(compundAmt):
                print "Interval: " + str(n) + "     Time passed: " + str(n*time) + "     End amount: " + str(startAmount * ((1 + rate)**n))
        except NameError:
            #Error checking
            print "Remember to input numerical values"
except KeyboardInterrupt:
    pass


