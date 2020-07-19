# Euler -- problem 01

def isMultiple(x):
	if(((x%3)==0) or ((x%5)==0)):
		return True
	else:
		return False


print(isMultiple(10))