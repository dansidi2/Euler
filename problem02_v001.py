def fib(n):
	if(n<1):
		return 1
	else:
		return (fib(n-1)+fib(n-2))

#for n in range(10):
#	print("fib({0}) = {1}".format(n, fib(n)))

fibs = []

for n in range(100):
	candidate = fib(n)
	if candidate > 3999999:
		break
	else:
		fibs.append(candidate)

print(fibs)

total = 0
for element in fibs:
	if((element%2) == 0):
		total += element
	else:
		total += 0

print("total = {0}".format(total))
