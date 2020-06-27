

class Node:
	def __init__(self, value=None):
		self.value = value
		self.next = None

class Linkedlist:
	def __init__(self):
		self.headval = None

	def start_add(self, value):
		new_node = Node(value)
		new_node.next = self.headval
		self.headval = new_node

	def end_add(self, value):
		new_node = Node(value)
		if(self.headval is None):
			self.headval = new_node
			return
		n = self.headval
		while(n.next):
			n = n.next
		n.next = new_node

	def print(self):
		printvalue = self.headval
		while(printvalue is not None):
			print(printvalue.value)
			printvalue = printvalue.next

	def reverse(self):
		prev = None
		current = self.headval
		following = current.next
		while(current is not None):
			current.next = prev
			prev = current
			current = following
			if(following is not None):
				following = following.next
		self.headval = prev						

list = Linkedlist()
list.headval = Node('5')
node2 = Node('6')
node3 = Node('7')
list.headval.next = node2
node2.next = node3
list.start_add('4')
list.end_add('8')		
list.reverse()
list.print()

