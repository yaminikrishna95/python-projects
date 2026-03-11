class Animal:
	def __init__(self,name):
		self.name=name
		self.is_alive=True

	def eating(self):
		print(f"{self.name} is Eating animal")
	def sleep(self):
		print(f"{self.name} is Sleeping ")

class Dog(Animal):
	def speak(self):
		print(f"{self.name} barks BOW BOWW")
class Cat(Animal):
	def speak(self):
		print("Meow Meow")
class Mouse(Animal):
	pass



dog= Dog("Scooby")
cat =Cat("Garfield")
mouse =Mouse("Bob")
dog.speak()
cat.speak()