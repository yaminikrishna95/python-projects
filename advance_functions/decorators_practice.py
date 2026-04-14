import logging


def my_logger(original_function):
	logging.basicConfig(filename='{}.log'.format(original_function.__name__),level=logging.INFO)

	def wrapper(*args, **kwargs):
		logging.info('{} called'.format(original_function.__name__))
		print('{} called'.format(original_function.__name__))
		return original_function(*args, **kwargs)

	return wrapper

@my_logger
def my_add(a, b):
	return a+b


@my_logger
def my_subtract(a, b):
	return a - b

print(my_add(1,2))
print(my_subtract(5,3))
