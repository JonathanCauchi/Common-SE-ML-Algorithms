
## brute force method, doesnt work on large numbers

dict = {}
number = int(input())
sum = 0
for i in range(1,number+1):
	sum += i
	dict.update({i:sum})

list = [i for i in dict.values()]

dict_factor = {}
for j in list:
	sum_factor = 0
	for k in range(1,int(j)+1):
		if(int(j)%k == 0):
			sum_factor += 1
			dict_factor.update({j:sum_factor})

print(dict_factor)
list = [i for i,j in dict_factor.items() if j>5]
print(list)
