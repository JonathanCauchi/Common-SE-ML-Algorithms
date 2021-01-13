import numpy as np

array = [1,2,3,4,5,6,7]
rotation = int(input("Enter no of rotations: "))
length = len(array)
new_array = []
for i in array:
    new_array.append(i)
#new_array = np.random.randint(1,11,length)
for i in range(length):
    if(i>=0 and i<(length-rotation)):
        new_array[i+rotation] = array[i]
    elif(i>=(length-rotation)):
        diff = length - rotation
        final = i - diff
        new_array[final]= array[i]
        
for i in new_array:
    print(i)
        
        
        
        
        
        
        
        
        
        
        
        