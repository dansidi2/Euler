# Euler -- problem 03
# find largest prime factor
def findMaxFactor(n):
	factors=[]
	for i in range(1, n):
		if(n%i == 0):
			if(i!=1):
				print("factor found! = {}".format(i))
				factors.append(i)
				n=n/i
		else:
			pass

	return max(factors)



print("max factor = {}".format(findMaxFactor(600851475143)))

