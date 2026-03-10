from six import raise_from


class Employee:
	num_of_emps = 0
	def __init__(self,first,last,pay):
		self.first = first
	raise_amount = 1.04
	def __init__(self,first,last,pay):
		self.first = first
		self.last = last
		self.pay=pay
		self.email = first +"."+last+"@company.com"
		Employee.num_of_emps+=1
	def fullname(self):
		return self.first+" "+self.last
	def apply_raise(self):
		self.pay = int(self.pay * self.raise_amount )
		return(self.pay)


print(Employee.num_of_emps)
emp_1 = Employee("James","Smith",50000)
emp_2 = Employee("laura","Smith",60000)
print(Employee.num_of_emps)
#print(emp_1.fullname())
#print(Employee.fullname(emp_1))
#print(emp_2.fullname())
emp_1.raise_amount = 1
#print(emp_1.apply_raise())
#print(Employee.apply_raise(emp_2))
#print(Employee.__dict__)
print(emp_1.__dict__)
print(emp_2.__dict__)
print(emp_2.raise_amount)
print(Employee.raise_amount)
print(emp_1.raise_amount)
print(Employee.apply_raise(emp_2))
