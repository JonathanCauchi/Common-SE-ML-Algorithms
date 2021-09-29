#from search import Problem
import numpy as np
import random
import sys

class PlusPuzzle: #extend here
    
  copy_list = None

  def __init__(self, start, list, goal=None):
    #Problem.__init__(self,start,list,goal)
    self.start = start
    self.list = list
    self.mid_value = None
    self.start_state = (1,0)
    self.empty_squares = [(0,1),(1,2),(2,1)]

  def assign_mid_value(self):
    self.copy_list = self.list
    self.copy_list.sort()
    index = round(len(self.copy_list)/2)
    self.mid_value = self.copy_list.pop(index) 
    self.start[1][1] = self.mid_value
    print("Assigning mid value {} to coordinates (1,1)".format(self.mid_value))
    print(self.start)
    random.shuffle(self.copy_list)

  def fill_matrix(self): #brute force method, trying out all possible combinations
    
    def fill_first_state():
      value = self.copy_list.pop(0)     
      self.start[self.start_state[0]][self.start_state[1]] = value
      print("Assigning {} at initial coordinate {}".format(value,self.start_state))
      print(self.start)

    fill_first_state() 

    coordinate = self.empty_squares[0]
    next_coordinate = self.empty_squares[1]
    last_coordinate = self.empty_squares[2]
    
    for i in range(0,6): # 6 total unique combinations (3 elements, 3 spaces)
      random_list = self.copy_list
      if(i==0 or i==1): #first two iterations, assign same element in same coordinate
        matrix_instance = self.start 
        matrix_instance[coordinate[0]][coordinate[1]] = random_list[0]
        #print("")
        if(i==0):
          print("-----------------")
          print("First combination")
          print("-----------------")
          value = random_list[1]
          matrix_instance[next_coordinate[0]][next_coordinate[1]] = value
          print("Inserting {} at coordinate {}".format(value,next_coordinate))
          print(matrix_instance)
          matrix_instance[last_coordinate[0]][last_coordinate[1]] = random_list[2]
          print("Inserting {} at coordinate {}".format(random_list[2],last_coordinate))
          print(matrix_instance)
          self.is_goal(matrix_instance)
        elif(i==1):
          print("-----------------")
          print("Second combination")
          print("-----------------")
          value = random_list[2]
          matrix_instance[next_coordinate[0]][next_coordinate[1]] = value
          print("Inserting {} at coordinate {}".format(value,next_coordinate))
          print(matrix_instance)
          matrix_instance[last_coordinate[0]][last_coordinate[1]] = random_list[1]
          print("Inserting {} at coordinate {}".format(random_list[1],last_coordinate))
          print(matrix_instance)
          self.is_goal(matrix_instance)
          

      elif(i==2 or i==3):
        matrix_instance = self.start
        matrix_instance[coordinate[0]][coordinate[1]] = random_list[1]
        if(i==2):
          print("-----------------")
          print("Third combination")
          print("-----------------")
          value = random_list[0]
          matrix_instance[next_coordinate[0]][next_coordinate[1]] = value
          print("Inserting {} at coordinate {}".format(value,next_coordinate))
          print(matrix_instance)
          matrix_instance[last_coordinate[0]][last_coordinate[1]] = random_list[2]
          print("Inserting {} at coordinate {}".format(random_list[2],last_coordinate))
          print(matrix_instance)
          self.is_goal(matrix_instance)       
        elif(i==3):
          print("-----------------")
          print("Fourth combination")
          print("-----------------")
          value = random_list[2]
          matrix_instance[next_coordinate[0]][next_coordinate[1]] = value
          print("Inserting {} at coordinate {}".format(value,next_coordinate))
          print(matrix_instance)
          matrix_instance[last_coordinate[0]][last_coordinate[1]] = random_list[0]
          print("Inserting {} at coordinate {}".format(random_list[0],last_coordinate))
          print(matrix_instance)
          self.is_goal(matrix_instance) 

      elif(i==4 or i==5):
        matrix_instance = self.start
        matrix_instance[coordinate[0]][coordinate[1]] = random_list[2]
        if(i==4):
          print("-----------------")
          print("Fifth combination")
          print("-----------------")
          value = random_list[0]
          matrix_instance[next_coordinate[0]][next_coordinate[1]] = value
          print("Inserting {} at coordinate {}".format(value,next_coordinate))
          print(matrix_instance)
          matrix_instance[last_coordinate[0]][last_coordinate[1]] = random_list[1]
          print("Inserting {} at coordinate {}".format(random_list[1],last_coordinate))
          print(matrix_instance)
          self.is_goal(matrix_instance)
        elif(i==5):
          print("-----------------")
          print("Sixth combination")
          print("-----------------")
          value = random_list[1]
          matrix_instance[next_coordinate[0]][next_coordinate[1]] = value
          print("Inserting {} at coordinate {}".format(value,next_coordinate))
          print(matrix_instance)
          matrix_instance[last_coordinate[0]][last_coordinate[1]] = random_list[0]
          print("Inserting {} at coordinate {}".format(random_list[0],last_coordinate))
          print(matrix_instance)
          self.is_goal(matrix_instance)

  def is_goal(self, matrix):
          
      vertical_sum = int(matrix[0][1]) + int(matrix[1][1]) + int(matrix[2][1])
      horizontal_sum = int(matrix[1][0]) + int(matrix[1][1]) + int(matrix[1][2])

      if(vertical_sum == horizontal_sum):
          print("GOAL REACHED!")
          print("Both horizontal and vertical sums are {}".format(vertical_sum))
          sys.exit()


start = np.array([['a',0,'a'],[0,0,0],['a',0,'a']]) #a is some arbitrary number given to the columns
list = [1,2,3,4,5]
#goal = np.array([['a',2,'a'],[1,3,5],['a',4,'a']]) 
obj = PlusPuzzle(start,list, None)
obj.assign_mid_value()
obj.fill_matrix()

  
