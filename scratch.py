def multiplyAllTheNumbers(n):
	total=1
	for i in n:
		total*=i
	return total


def listFactors(n):
	factors=[]
	for i in range(1, n):
		if(n%i==0):
			factors.append(i)
			n=n//i
		
	return factors

def muliplyFactors(factors):
	total = 1
	for i in factors:
		print("{} x ".format(i))
		total*=i
	return total

def isPrime(n):
	for i in range(2, n):
		if(n%i==0):
			return False
	return True



def listPrimes(n):
	primes=[]
	for i in range(2, n):
		if isPrime(i):
			primes.append(i)
	return primes



# print("multiplyAllTheNumbers(10): {}".format(multiplyAllTheNumbers(10)))
# print("listFactors: {}".format(listFactors(multiplyAllTheNumbers(10))))
numberList=[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print("multiply numberList: {}".format(multiplyAllTheNumbers(numberList)))

# print("listFactors(9699690): {}".format(listFactors(9699690)))

# print("listPrimes: {}".format(listPrimes(10)))

# print("muliply primes: {}".format(multiplyAllTheNumbers(listPrimes(20))))

# primes up to 10: 1, 2, 3, 5, 7

#num = 2520
#print("factors of {}: {}".format(num, listFactors(num)))
#print("muliply factors: {}".format(muliplyFactors(listFactors(num))))
#print("{} / {}: {}".format(num, muliplyFactors(listFactors(num)), (num//muliplyFactors(listFactors(num)))))
