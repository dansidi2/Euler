# Euler -- problem 01

def isMultiple(x):
	if(((x%3)==0) or ((x%5)==0)):
		return True
	else:
		return False


def findMultiples(n):
	multiples = []
	for i in range(n):
		if isMultiple(i):
			multiples.append(i)
	print(multiples)
	return multiples

def addMultiples(target):
	total = 0
	multiples = findMultiples(target)
	for item in multiples:
		total += item
	return total

print(addMultiples(1000))
