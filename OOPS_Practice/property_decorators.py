class Employee:

	def __init__(self,first,last,pay):
		self.first = first
		self.last = last
		self.pay = pay

	def email(self):
		return self.first + "." + self.last + "@gmail.com"
	def fullname(self):
		return self.first + " " + self.last


emp_1=Employee("James","Smith",50000)
emp_1.first="Jim"
print(emp_1.first)
print(emp_1.email())
print(emp_1.fullname())

