
class Node:
	def __init__(self,value=None):
		self.value = value
		self.next = None

#LIFO	
class Stack:
	def __init__(self):
		self.tail = None

	def isempty(self):
		if(self.tail == None):
			print("Empty List")
			return True
		else:
			print("Non-Empty List")
			return False

	def push(self,value):
		if(self.tail == None):
			self.tail = Node(value)
		else:
			new_node = Node(value)
			new_node.next = self.tail
			self.tail = new_node	
	
	def peek(self): #print last element
		current = self.tail
		if(self.isempty()):
			print("List is empty")
		else:
			print(current.value)
	
	def pop(self): #remove last entry
		current = self.tail
		if(self.isempty()):
			print("List is empty")
		else:
			pop_node = current
			self.tail = self.tail.next
			pop_node.next = None
			return pop_node.value
			
						

	def printlist(self):
		current = self.tail
		while(current):
			print(current.value)
			current = current.next
stack = Stack()
stack.tail = Node('3')
stack.push('4')
stack.push('5')
stack.pop()
stack.printlist()
