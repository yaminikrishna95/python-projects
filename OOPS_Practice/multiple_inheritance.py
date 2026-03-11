class Animal:
    def __init__(self, name):
        self.name = name

    def eat(self):
        print(f"{self.name} is eating")

    def sleep(self):
        print(f"{self.name} is sleeping")


class Prey(Animal):
    def flee(self):
        print(f"{self.name} is fleeing")


class Predator(Animal):
    def hunt(self):
        print(f"{self.name} is hunting")


class Rabbit(Prey):
    pass


class Hawk(Predator):
    pass


class Fish(Prey, Predator):
    pass


# Creating objects
rabbit = Rabbit("Bug")
hawk = Hawk("Sky Hunter")
fish = Fish("Nemo")

# Calling methods
rabbit.eat()
rabbit.flee()

hawk.eat()
hawk.hunt()

fish.eat()
fish.flee()
fish.hunt()