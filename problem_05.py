# Euler problem 05 - smallest number divisible by all numbers 1-20
# 2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.
# What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?

def factorial(n):
	fac = 1
	for i in range(1, n+1):
		fac *= i
	return fac

def getFactors(n):
	factors=[]
	for i in range(2, int(n ** 0.5)):
		if(n%i==0):
			factors.append(i)
	return factors

def isPrime(n):
	if(len(getFactors(n)) < 1):
		return True
	else:
		return False

def primeFactors(n):
	primeFactors=[]
	factors = getFactors(n)
	for i in factors:
		if(isPrime(i)):
			primeFactors.append(i)
	return primeFactors


def firstPrimes(n):
	primes = []
	i = 1
	while (len(primes) < n + 1):
		
		if isPrime(i):
			primes.append(i)
		i += 1
	return primes[-1]

print(f"firstPrimes(10001): {firstPrimes(10001)}")
