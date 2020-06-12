import sys
import math

x=0
y=0
p=0
q=0
flag = 0
print("Enter direction and unit\n")
print('Either UP, DOWN, LEFT or RIGHT, then space and a numerical unit\n')
print('If you want to stop write STOP\n')
while(flag == 0):
	usr_input = input().split()
	if usr_input[0].upper() == 'STOP':
		break
	if usr_input[0].upper() == 'UP':
		y += int(usr_input[1])
	if usr_input[0].upper() == 'DOWN':
                y -= int(usr_input[1])
	if usr_input[0].upper() == 'LEFT':
                x -= int(usr_input[1])
	if usr_input[0].upper() == 'RIGHT':
                x += int(usr_input[1])

output =  round(math.sqrt((x-q)**2 + (y-p)**2))
print(output)
