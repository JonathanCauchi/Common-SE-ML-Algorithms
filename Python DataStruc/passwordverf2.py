import re
#Regex is the way to go

def main():
	usr_input = input().split(",")
	list = []
	for i in usr_input:
		count = 0
		count += len(i) > 5 and len(i) < 13
		count += bool(re.search("[A-Z]",i))
		count += bool(re.search("[a-z]",i))
		count += bool(re.search("[@$#]",i))
		count += bool(re.search("[0-9]",i))
		if(count == 5):
			list.append(i)
	print(",".join(list))

main()
