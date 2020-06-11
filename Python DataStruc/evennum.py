
list = []
for i in range(1000,3001):
	i = str(i)
	size = len(i)
	count = 0
	for j in range(0,size):
		if(int(i[j])%2==0):
			count = count + 1
	if(count == size):
		list.append(i)
print(list)
