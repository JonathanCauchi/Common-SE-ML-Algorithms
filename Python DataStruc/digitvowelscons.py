input = input()
dict ={"DIGIT":0, "VOWELS":0, "CONSONANTS":0}
for i in input:
	if(i == '1' or i =='2' or i =='3'or i=='4' or i=='5'or i=='6'or i=='7' or i=='8' or i=='9' or i=='0'):
		dict["DIGIT"]+=1
	elif(i=='a' or i=='e' or i=='i' or i=='o' or i=='u'):
		dict["VOWELS"]+=1
	elif(i==' '):
		pass
	else:
		dict["CONSONANTS"]+=1
print("Num of Digitd:\n",dict["DIGIT"])
print("Num of Vowels:\n",dict["VOWELS"])
print("Nun of Consonants & special chars:\n",dict["CONSONANTS"])

-----------------------------------------------------------------------

for i in input:
	if(i.isdigit()):
		dict["DIGIT"]+=1

