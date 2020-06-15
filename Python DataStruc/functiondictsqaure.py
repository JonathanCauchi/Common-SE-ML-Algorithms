
def printdict(n):
	dict = {i: i**2 for i in range(1,n+1)}
	print(dict)

num = int(input("Enter number:\n"))
printdict(num)
