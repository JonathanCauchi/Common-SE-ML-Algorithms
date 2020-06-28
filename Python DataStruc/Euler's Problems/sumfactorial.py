



def factorial(n):
	if(n == 1):
		return 1
	else:
		return n*factorial(n-1)

def main():
	num = int(input("Enter digit:"))
	result = factorial(num)
	str_result = str(result)
	total = 0
	for i in range(len(str_result)):
		total += int(str_result[i])
	print("Factorial is: ", result)
	print("-------------------------")
	print("Sum of factorial digits is: ",total)

main()
	
