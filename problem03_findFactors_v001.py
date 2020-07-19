# Euler -- problem 03
# find factors of n

def findFactors(n):
	factors=[]
	for i in range(1, n):
		if(n%i == 0):
			print("factor found! = {}".format(i))
			if(i!=1):
				factors.append(i)
				n=n/i
		else:
			pass

	print(factors)

findFactors(13195)