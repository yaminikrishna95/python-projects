"""def square_numbers(nums):
    for num in nums:
        yield num**2

my_nums=square_numbers([1,2,3,4,5])
print(my_nums)
for i in my_nums:
    print(i)
"""
import random
import time

names=['John','Corey','Adam']
majors=['Math','Engineering']

def people_list(num_people):
	result=[]
	for i in range(num_people):
		person={
			'id' :i,
		     'name':random.choice(names),
			 'major':random.choice(majors)
		}
	result.append(person)
	return result

def people_list(num_people):

	for i in range(num_people):
		person={
			'id' :i,
		     'name':random.choice(names),
			 'major':random.choice(majors)
		}

	yield result


t1=time.clock()
people=people_list(1000000)
t2=time.clock()