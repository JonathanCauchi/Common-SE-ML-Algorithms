
class Flight:

	counter = 1
	
	def __init__(self,origin,destination,duration):
		self.origin = origin
		self.destination = destination
		self.duration = duration
		self.passengers = []
		self.ID = Flight.counter
		Flight.counter += 1
	
	def delay(self, amount):
		self.duration += amount

	def add_passenger(self, p):
		self.passengers.append(p)

	def print_pass(self):
		for passenger in self.passengers:
			print(f"{passenger.name}")

class Passenger:
	def __init__(self,name):
		self.name = name

flight = Flight("Malta","Catania",30)
pass1 = Passenger("Jonathan")
flight.add_passenger(pass1)
flight.print_pass()
print(flight.__dict__)
