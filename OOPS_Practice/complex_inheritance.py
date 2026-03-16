class Employee:
	num_of_emps = 0


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

class Manager(Employee):
	def __init__(self,first,last,pay,employees=None):
		super().__init__(first,last,pay)
		self.employees = employees


emp_1 = Employee("James","Smith",50000)
emp_2 = Employee("laura","Smith",60000)

mgr_1= Manager("John","Doe",80000,[emp_1])
print(isinstance(Manager,Employee))

print(mgr_1.fullname())
print(mgr_1.email)