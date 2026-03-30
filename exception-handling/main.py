"""try:

	a=b
	result =1/0

except NameError as ex:
	print(ex)


try:
	result=1/0
except ZeroDivisionError as ex:
	   print(ex)
	   print("Enter valid Denominator")



try:
	result=1/2
	a=b
except ZeroDivisionError as ex:
	print(ex)
	print("Enter valid Denominator")
except Exception as ex1:
	print(ex1)
	print("main exception got caught here")
"""
"""
try:
	number=int(input("Enter a number"))
	result=10/number
except ValueError:
	   print("Enter a valid number")
except ZeroDivisionError as ex:
	   print("Enter denomitor grater than zero")
except Exception as ex:
	   print(ex)


try:
	num=int(input("Enter a number"))
	result=10/num
except ValueError:
	   print("Enter a valid number")
except ZeroDivisionError as ex:
	   print("Enter denomitor grater than zero")
except Exception as ex:
	   print(ex)
else:
	   print(f"The result is {result}") """
"""
try:
	num=int(input("Enter a number"))
	result=10/num
except ValueError:
	   print("Enter a valid number")
except ZeroDivisionError as ex:
	   print("Enter denomitor grater than zero")
except Exception as ex:
	   print(ex)
else:
	   print(f"The result is {result}")
finally:
	   print("Execution comoplete")



try:
	file=open('example.txt','r')
	context=file.read()
	print(context)
except FileNotFoundError:
	print("File not found")
finally:
	if 'file' in locals() or not file.closed():
		file.close()
		print("File closed")
"""


