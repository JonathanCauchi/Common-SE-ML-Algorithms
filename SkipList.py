# Author Kalci
# Description Python3code operations for skip list 

import random 
import math

class Node(object): 
    #Class for Node
    def __init__(self, key, level): 
        self.key = key 

        # list to hold references to node of different level 
        self.forward = [None]*(level+1) 

class SkipList(object): 
     
    #Class for Skip list 
    
    def __init__(self, max_lvl, P): 
        # Maximum level for this skip list 
        self.MAXLVL = max_lvl 

        # P is the fraction of the nodes with level 
        # i references also having level i+1 references 
        self.P = P 

        # create header node and initialize key to -1 
        self.header = self.createNode(self.MAXLVL, -1) 

        # current level of skip list 
        self.level = 0
    
    # create new node 
    def createNode(self, lvl, key): 
        n = Node(key, lvl) 
        return n 
    
    # create random level for node 
    def randomLevel(self): 
        lvl = 0
        while random.random()<self.P and lvl<self.MAXLVL:
            lvl += 1
        return lvl 

    # insert given key in skip list 
    def insertElement(self, key): 
        # create update array and initialize it 
        update = [None]*(self.MAXLVL+1) 
        current = self.header 

        ''' 
        start from highest level of skip list 
        move the current reference forward while key 
        is greater than key of node next to current 
        Otherwise inserted current in update and 
        move one level down and continue search 
        '''
        for i in range(self.level, -1, -1): 
            while current.forward[i] and current.forward[i].key < key: 
                current = current.forward[i] 
            update[i] = current 

        ''' 
        reached level 0 and forward reference to 
        right, which is desired position to 
        insert key. 
        '''
        current = current.forward[0] 

        ''' 
        if current is NULL that means we have reached 
        to end of the level or current's key is not equal 
        to key to insert that means we have to insert 
        node between update[0] and current node 
        '''
        #if current == None : # or current.key != key:
        # Generate a random level for node
        rlevel = self.randomLevel()
        '''
            If random level is greater than list's current 
            level (node with highest level inserted in 
            list so far), initialize update value with reference 
            to header for further use 
        '''
        if rlevel > self.level: 
            for i in range(self.level+1, rlevel+1): 
                update[i] = self.header 
            self.level = rlevel 

        # create new node with random level generated 
        n = self.createNode(rlevel, key) 
        # insert node by rearranging references 
        for i in range(rlevel+1): 
            n.forward[i] = update[i].forward[i] 
            update[i].forward[i] = n 

        #print("Successfully inserted key {}".format(key)) 

    def deleteElement(self, search_key): 

        # create update array and initialize it 
        update = [None]*(self.MAXLVL+1) 
        current = self.header 

        ''' 
        start from highest level of skip list 
        move the current reference forward while key 
        is greater than key of node next to current 
        Otherwise inserted current in update and 
        move one level down and continue search 
        '''
        for i in range(self.level, -1, -1): 
            while(current.forward[i] and current.forward[i].key < search_key): 
                current = current.forward[i] 
            update[i] = current 

        ''' 
        reached level 0 and advance reference to 
        right, which is prssibly our desired node 
        '''
        current = current.forward[0] 

        # If current node is target node 
        if current != None and current.key == search_key: 
            ''' 
            start from lowest level and rearrange references 
            just like we do in singly linked list 
            to remove all target node with search_key
            '''
            while current and current.key == search_key :
                for i in range(self.level+1): 

                    ''' 
                    If at level i, next node is not target 
                    node, break the loop, no need to move 
                    further level 
                    '''
                    if update[i].forward[i] != current: 
                        break
                    update[i].forward[i] = current.forward[i] 

                # Remove levels having no elements 
                while(self.level>0 and self.header.forward[self.level] == None): 
                    self.level -= 1
                current = current.forward[0]
            print("Successfully deleted {}".format(search_key))
            return True
        else:
            print("Delete Failure! {}".format(search_key))
            return False

    def searchElement(self, key): 
        current = self.header 

        ''' 
        start from highest level of skip list 
        move the current reference forward while key 
        is greater than key of node next to current 
        Otherwise inserted current in update and 
        move one level down and continue search 
        '''
        find_step=0
       
        for i in range(self.level, -1, -1): 
            while(current.forward[i] and current.forward[i].key < key): 
                current = current.forward[i]
                find_step=find_step+ 1

        # reached level 0 and advance reference to 
        # right, which is prssibly our desired node 
        current = current.forward[0] 

        # If current node have key equal to 
        # search key, we have found our target node 
        if current and current.key == key: 
            print("\nFound key ", key)
            print("Find Step",find_step)
            #find index of x
            current=self.header
            find_index=0
            #search index
            while (current.forward[0] and current.forward[0].key<key):
                current=current.forward[0]
                find_index=find_index+1
            # pringt all indeics with key
            current = current.forward[0]
            all_index = []
            while current.key == key :
                all_index.append(find_index)
                current = current.forward[0]
                find_index += 1
            print("Find index", all_index)
            return find_index
        else:
            print("\nNot Found", key)
            return -1

    def getLength(self):
        length=0
        head = self.header
        node=head.forward[0]
        while(node!=None): 
            node = node.forward[0]
            length=length+1
        return length
    
    def getLevel(self):
        return self.level

    def getElementByIndex(self,index):
        head=self.header
        current=head.forward[0]
        if index<self.getLength():
            for i in range(0,index):
                current=current.forward[0]
            return current.key
        else:
            print("Error!")
            return -1
            #print("The integer stored at ",index,"is",current.key)
            

    # Display skip list level wise 
    def displayList(self): 
        print("\n*****Skip List******") 
        head = self.header 
        for lvl in range(self.level+1): 
            print("Level {}: ".format(lvl), end=" ")            
            node = head.forward[lvl] 
            while(node != None): 
                print(node.key, end=" ") 
                node = node.forward[lvl]                
            print("") 

# Driver to test above code 
def main():
    #initialise the empty skip list
    p=1/2
    numOfElement=1000
    #Get MAX_LEVEL
    MAX_LEVEL=(int)(math.log(numOfElement)/math.log(1/p))

    #1. Initialize skip list
    print(" 1. Initializng the skip list")
    lst = SkipList(MAX_LEVEL, p)
    
    #2. insert 1,000 random integers each in the range 0 to 512 inclusive.
    print("\n 2. Insert 1,000 random integers into skip list")
    for i in range(1000):
        #create a random integer x in the range 0 to 512
        p = random.randint(0,512)
        #insert to skip list
        lst.insertElement(p)
    #display list
    lst.displayList()

    print("\n 3. For 10 times, create a random integer x in the range 0 to 512 and Find that number x in the skip list.")
   
    # 3. For 10 times, create a random integer x in the range 0 to 512
    # Find that number x in the skip list.
    
    for i in range(10):
        p=random.randint(0,512)
        lst.searchElement(p)

    print("\n 4. For 10 times, create a random integer x in the range 0 to length of skiplist-1 and return the integer stored at index x")
    # 4. For 10 times, create a random integer x in the range 0 to length
    #    of skiplist-1 and return the integer stored at index x
   
    for i in range(10):
        p=random.randint(0,lst.getLength())
        print(p,"th element is ",lst.getElementByIndex(p))

    print("\n 5. For 10 times, Create a random integer x in the range 0 to 512. Delete all instances of that number x in the skip list")
    # 5. For 10 times, Create a random integer x in the range 0 to 512
    # Delete all instances of that number x in the skip list
    for i in range(10):
        p=random.randint(0,512)
        lst.deleteElement(p)
    print("\n 6. For 10 times: Create a random integer x in the range 0 to length and delete the integer stored at index x")
    #6. For 10 times: Create a random integer x in the range 0 to length and delete
    #   the integer stored at index x

    for i in range(10):
        p=random.randint(0,lst.getLength())
        lst.deleteElement(lst.getElementByIndex(p))
    
    # 7. Display the length (number of items) of the skip list
    print("\n 7. The length of Skip list is ",lst.getLength())

    # 8. Display the height of the skip list
    print("\n 8. Height of Skip list is ",lst.getLevel())
   
if __name__ == '__main__':
    main() 
