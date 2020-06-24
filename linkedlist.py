class Node:
	def __init__(self, value=None):
		self.datavalue = value
		self.nextvalue = None

class LinkedList:
	def __init__(self):
		self.headval = None	

	#traversing a list
	def listprint(self): 
		printvalue = self.headval
		while(printvalue is not None):
			print(printvalue.datavalue)
			printvalue = printvalue.nextvalue

	def addnodestart(self, value):
		new_node = Node(value)
		new_node.nextvalue = self.headval
		self.headval = new_node
	
	
	def addnodeend(self,value):
		new_node = Node(value)
		if(self.headval is None):
			self.headval = new_node
			return
		find_last = self.headval
		while(find_last.nextvalue):
			find_last = find_last.nextvalue

	def remove(self, value):

		HEAD = self.headval		

		if(HEAD is None):
			print("Linked List is empty, populate it first")
			return

		if(HEAD is not None):
			if(HEAD.datavalue == value):
				self.headval = HEAD.next
				HEAD = None
				return
			
 

list = LinkedList()
list.headval = Node("Monday")
node2 = Node("Tuesday")
node3 = Node("Wednesday")
list.headval.nextvalue = node2
node2.nextvalue = node3
list.addnodestart("Sunday")
list.addnodeend("Thursday")

list.listprint()
