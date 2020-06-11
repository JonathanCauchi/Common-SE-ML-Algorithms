list = input().split(",")
list = [int(i) for i in list]	
output = []
for i in list:
	i = i*i
	output.append(i)
output = [str(i) for i in output]
print(",".join(output))
