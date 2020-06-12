class Generator():

	def __init__(self,n):
		self.n = n

	def generate(self):
		for i in range(1,(self.n)+1):
			if(i%7==0):
				yield i	

test = Generator(int(input("Enter range:")))
iterator = test.generate()
for i in iterator:
	print(i)
