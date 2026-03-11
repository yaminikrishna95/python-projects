class Animal:
	def __init__(self,name):
		self.name=name
		self.is_alive=True

	def eating(self):
		print(f"{self.name} is Eating animal")
	def sleep(self):
		print(f"{self.name} is Sleeping ")

class Dog(Animal):
	pass
class Cat(Animal):
	pass
class Mouse(Animal):
	pass



dog= Dog("Scooby")
cat =Cat("Garfield")
mouse =Mouse("Bob")
dog.eating()
cat.sleep()
mouse.eating()