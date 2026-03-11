class Animal:
	def eat(self):
		print("Eating animal")
	def sleep(self):
		print("Sleeping animal")

class Prey(Animal):
	def flee(self):
		print("This animal is fleeing")


class Predator(Animal):
	def hunt(self):
		print("This animal is hunting")

class rabbit(Prey):
	pass

class hawk( Predator):
	pass

class Fish(Prey, Predator):

	pass

Rabbit= rabbit()
hawk=  hawk()
Fish = Fish()

Fish.eat()