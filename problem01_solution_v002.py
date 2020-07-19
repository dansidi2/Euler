# Euler -- problem 01 -- solution

def sumDivisibleBy(target, n):
	p = target // n
	print("p({0}) = {1}".format(n, p))

	sum = n*(p*(p+1)) // 2

	return sum

def getTotal(target):
	total = (sumDivisibleBy(target, 3) + sumDivisibleBy(target, 5) - sumDivisibleBy(target, 15))
	return total

print(getTotal(9999))

