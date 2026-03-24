from zmq.backend import first


class Employee:

	def __init__(self,first,last,pay):
		self.first = first
		self.last = last
		self.pay = pay
	@property
	def email(self):
		return '{}.{}@gmail.com'.format(self.first,self.last)
	@property
	def fullname(self):
		return self.first + " " + self.last

	@fullname.setter
	def fullname(self,name):
		first,last = name.split(" ")
		self.first = first
		self.last = last
	@fullname.deleter
	def fullname(self):
		print("Deleting employee fullname")
		self.first=None
		self.last=None



emp_1=Employee("James","Smith",50000)

emp_1.first="Jim"

print(emp_1.first)
print(emp_1.email)
print(emp_1.fullname)


