def isprime(num):
	for i in range(2,int(num**0.5)+1):
		if(num % i == 0):
			return False
	return True
	
	
	

def main():
	num = 2000000
	sum = 2	
	for i in range(3,num+1):
		if(isprime(i) == True):
			sum += i
	print(sum)	

main()
