



## applying reduce (functional style)
from functools import reduce

def factors(n):    
    return set(reduce(list.__add__, 
                ([i, n//i] for i in range(1, int(n**0.5) + 1) if n % i == 0)))

def main():
	dict = {}
	number = int(input())
	sum = 0
	for i in range(1,number+1):
        	sum += i
        	dict.update({i:sum})

	list = [i for i in dict.values()]
	dict_factor = {}
	for j in list:
        	count = factors(j)
        	dict_factor.update({j:len(count)})            
	list = [i for i,j in dict_factor.items() if j>500]
	print(list)

main()








