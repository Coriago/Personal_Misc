try:
    while True:
        limit = input("maximum multiple limit: ")
        nums = range(limit, 1, -1)
        multiples1 = []
        multiples2 = []
        multsum = 0
        for number in nums:
            if (number % 3) == 0:
                multiples1.append(number)
            if (number % 5) == 0:
                multiples2.append(number)
        totalmultiples = multiples1 + multiples2
        for y in totalmultiples:
            if totalmultiples.count(y) > 1:
                totalmultiples.remove(y)
        totalmultiples.sort()
        for n in totalmultiples:
            multsum = multsum + n
        print "sum of multiples of 3 and 5 for given limit = " + str(multsum)
except KeyboardInterrupt:
    pass
