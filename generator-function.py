#learn how to use generator function

def isprime(n):
	if n == 1:
		return False;

	for x in range(2, n):
		if n % x == 0:
			return False

	else:
		return True


# This is a generator number
def primes(n = 21):
 	while(True):
 		if isprime(n): yield n
 		n += 1


#calling function
for n in primes():
	if n > 100: break
	print(n)