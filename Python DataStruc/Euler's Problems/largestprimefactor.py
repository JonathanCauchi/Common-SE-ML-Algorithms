##Python is so fucking slow

def isprime(num):
	for i in range(2, int(num**0.5)+1):
		if(num % i == 0):
			return False
	return True

def main():
	num = 600851475143
	list_prime = []
	for i in range(2,num+1):
		if(isprime(i)==True):
			if(num % i == 0):
				list_prime.append(i)
			else:
				continue

	print(max(list_prime))
		
	
main()
