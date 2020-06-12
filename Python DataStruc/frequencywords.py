
dict = {}
usr_input = input().split()
for i in usr_input:
	 dict.setdefault(i, usr_input.count(i))

dict = sorted(dict.items())

for i in dict:
	print("%s:%d" %(i[0],i[1]))
