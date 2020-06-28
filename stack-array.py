class Stack:
	def __init__(self):
		self.stack = []
	
	def isempty(self):
		return self.stack == []

	def push(self,data):
		self.stack.append(data)

	def pop(self):
		del self.stack[-1]

	def peek(self):
		print(self.stack[-1])

	def size_stack(self):
		print(len(self.stack))

stack = Stack()
stack.push('1')
stack.push('2')
stack.push('3')
print("Last element: \n")
stack.peek()
print("Size of stack: \n")
stack.size_stack()
print("Popping last elements off stack\n")
stack.pop()
print("Last element: \n")
stack.peek()

			
