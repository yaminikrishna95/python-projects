"""def decorator_functions(original_function):
	def wrapper_function():
	    print('wrapper executed this before {}'.format(original_function))
		return original_function()
	return wrapper_function


def display():
	print("Display Function Ran")


decorated_display = decorator_functions(display)


decorated_display()

"""
def decorator_functions(original_function):
	def wrapper_function(*args, **kwargs):
		print('wrapper executed this before {}'.format(original_function.__name__))
		return original_function(*args, **kwargs)

	return wrapper_function

class decorator_classes(object):
	def __init__(self, original_function):
		self.original_function = original_function
	def __call__(self, *args, **kwargs):
		print('call executed this before {}'.format(self))
		return self.original_function(*args, **kwargs)


@decorator_functions
def display():
	print("Display Function Ran")

@decorator_functions
def display_info(name,age):
	print("Display Function Ran with argumanets {} {}".format(name,age))

display_info('John',25)
display()