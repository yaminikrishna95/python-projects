from six import raise_from


class Employee:
	num_of_emps = 0

	raise_amount = 1.05
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

	@classmethod
	def set_raise_amount(cls,amount):
		cls.raise_amount = amount

	@classmethod
	def from_string(cls,emp_str):
		first,last,pay = emp_str.split("-")
		return cls(first,last,pay)
	@staticmethod
	def is_workday(day):
		if day.weekday()==5 or day.weekday()==6:
			return False
		return True



emp_1 = Employee("James","Smith",50000)
emp_2 = Employee("laura","Smith",60000)

emp_str_1="John-Doe-70000"
emp_str_1= Employee.from_string(emp_str_1)
print(emp_str_1.fullname())

import datetime
my_datetime = datetime.datetime(2026,9,11)
print(Employee.is_workday(my_datetime))




print(Employee.num_of_emps)
#print(emp_1.fullname())
#print(Employee.fullname(emp_1))
#print(emp_2.fullname())
emp_1.raise_amount = 2
print(emp_1.apply_raise())
#print(Employee.apply_raise(emp_2))
#print(Employee.__dict__)
#print(emp_1.__dict__)
#print(emp_2.__dict__)
#print(emp_2.raise_amount)
#print(Employee.raise_amount)
#print(emp_1.raise_amount)
#print(Employee.apply_raise(emp_2))
