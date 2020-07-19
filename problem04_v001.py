# Euler problem 04 - palindrome product

def isPalindrome(n):
	s=str(n)

	if(len(s)>1):
		if(s[0]==s[-1:]):
			return isPalindrome((s[1:-1]))
		else:
			return False
	else:
		return True

largest = 0
for i in range(999, 100, -1):
	for j in range(999, 100, -1):
		product = i*j
		if(isPalindrome(product)):
			if(product>largest):
				largest=product
			break
print("largest: {}".format(largest))