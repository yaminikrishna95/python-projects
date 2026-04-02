
def divide(a, b):
    try:
        result = a / b
    except ZeroDivisionError as e:
        print(f"Error: {e}")
        result = None
    finally:
        print("Execution complete.")
    return result

def read_file(filename):
    try:
        file = open(filename, 'r')
        content = file.read()
        return content
    except FileNotFoundError as e:
        print(f"Error: {e}")
    finally:
        try:
            file.close()
        except NameError:
            pass
def sum_list(lst):
    total = 0
    try:
        for item in lst:
            total += item
    except TypeError as e:
        print(f"Error: {e}")
        total = None
    finally:
        print("Execution complete.")
    return total
def get_integer():
    try:
        value = int(input("Enter an integer: "))
    except ValueError as e:
        print(f"Error: {e}")
        value = None
    finally:
        print("Execution complete.")
    return value

def nested_exception_handling(s):
    try:
        try:
            num = int(s)
        except ValueError as e:
            print(f"Conversion error: {e}")
            num = None
        finally:
            print("Conversion attempt complete.")
        if num is not None:
            try:
                result = 10 / num
            except ZeroDivisionError as e:
                print(f"Division error: {e}")
                result = None
            finally:
                print("Division attempt complete.")
            return result
    finally:
        print("Overall execution complete.")

import requests

def read_url(url):
    try:
        response = requests.get(url)
        response.raise_for_status()
        return response.text
    except requests.RequestException as e:
        print(f"Network error: {e}")
        return None
    finally:
        print("Execution complete.")
import json

def parse_json(json_string):
    try:
        data = json.loads(json_string)
        return data
    except json.JSONDecodeError as e:
        print(f"JSON error: {e}")
        return None
    finally:
        print("Execution complete.")
class NegativeNumberError(Exception):
    pass

def check_for_negatives(lst):
    try:
        for num in lst:
            if num < 0:
                raise NegativeNumberError(f"Negative number found: {num}")
    except NegativeNumberError as e:
        print(f"Error: {e}")
    finally:
        print("Execution complete.")
def risky_function():
    raise ValueError("An error occurred in risky_function.")

def safe_function():
    try:
        risky_function()
    except ValueError as e:
        print(f"Error: {e}")
    finally:
        print("Execution complete.")
def risky_function():
    raise ValueError("An error occurred in risky_function.")


def safe_function():
    try:
        risky_function()
    except ValueError as e:
        print(f"Error: {e}")
    finally:
        print("Execution complete.")
#print(divide(1, 2))
#print(divide(1, 0))
#print(read_file('data.txt'))
#print(sum_list([1, 2, 3, 'a']))  # None
#print(get_integer())
#print(read_url('https://nonexistent.url'))
#print(parse_json('Invalid JSON'))  # None
#check_for_negatives([1, -2, 3, 4])
safe_function()