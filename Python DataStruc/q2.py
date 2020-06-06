def main():
	num = int(input("Enter number"))
	result = factorial(num)
	print(result)
	
def factorial(n):
	if(n==0):
		return 1
	else:
		return n*factorial(n-1)

main()
