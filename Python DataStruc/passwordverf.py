def main():
	usr_input = input().split(",")   	
	usr_input = [str(i) for i in usr_input]
	output = []
	for i in usr_input:		
		if(str_size(i) and letter_low(i) and letter_upper(i) and num(i) and spechar(i)):
			output.append(i)
	print(",".join(output))
	

def str_size(str):
	if(len(str) > 5 and len(str) < 13):
		return True
	else:
		return False

def letter_low(str):
	for i in str:
		if(i >= "a" and i <= "z"):
			return True
		else:
			return False 

def letter_upper(str):
	for i in str:
		if(i >= "A" and i <= "Z"):
			return True
		else:
			return False 


def num(str):
	for i in str:
		if(i >= "0" and i <= "9"):
			return True
		else:
			return False 

def spechar(str):
	for i in str:
		if(i=='$' and i=='#' and i=='@'):
			return True
		else:
			return False

main()
