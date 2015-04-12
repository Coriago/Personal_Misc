def sup(base,power):        ##sum of digits of number with an exponent
	h = str(base**power)
	ds = 0      ##digit sum
	for g in h:
		ds += int(g)
	return ds
print sup(2,1000)       ##sum of the digits of 2^1000
