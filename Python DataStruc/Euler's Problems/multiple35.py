

def ismultiple(i,x,y):
	if(i%x == 0 or i%y == 0):
		return True
	else:
		return False




def main():
	x = 3
	y = 5
	limit = 1000
	sum = 0
	for i in range(x,limit):
		if(ismultiple(i,x,y)== True):
			sum += i
		else:
			continue
	print(sum)

main()
