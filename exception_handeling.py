#==================================================================================
# EXCEPTION HANDLING IN PYTHON
#==================================================================================
"""
NOTES:
- Exception is an error that occurs during program execution
- Exception handling prevents program from crashing
- Allows graceful error handling and recovery
- Uses try-except blocks
"""

#==================================================================================
# WHAT ARE EXCEPTIONS?
#==================================================================================
"""
NOTES:
- Exceptions are runtime errors
- They stop normal program flow
- Python raises exceptions when something goes wrong
- Without handling, program crashes
"""

# Example of error without handling
print("--- PROGRAM WITHOUT EXCEPTION HANDLING ---")
print("Program starts")
print("Doing some calculations...")
# num = 10 / 0  # This will crash the program - ZeroDivisionError
# print("This line won't execute")
print("(Division by zero would crash here)\n")

#==================================================================================
# TRY-EXCEPT BLOCK (BASIC)
#==================================================================================
"""
NOTES:
- try block contains code that might cause error
- except block handles the error
- If error occurs in try, except block executes
- If no error, except block is skipped
- Program continues after try-except
"""

# Basic try-except
print("--- BASIC TRY-EXCEPT ---")
print("Program starts")

try:
    result = 10 / 0
    print("Result:", result)
except:
    print("An error occurred!")

print("Program continues after exception\n")

# Another example
print("Example 2:")
try:
    number = int("abc")
    print("Number:", number)
except:
    print("Cannot convert 'abc' to integer")
    
print("Program still running\n")

#==================================================================================
# SPECIFIC EXCEPTION TYPES
#==================================================================================
"""
NOTES:
- Better to catch specific exceptions
- Different exceptions for different errors
- Makes error handling more precise
- Can handle different errors differently
"""

# ZeroDivisionError
print("--- SPECIFIC EXCEPTIONS ---")
print("Example 1: ZeroDivisionError")

try:
    result = 10 / 0
except ZeroDivisionError:
    print("Error: Cannot divide by zero!")

print()

# ValueError
print("Example 2: ValueError")

try:
    number = int("hello")
except ValueError:
    print("Error: Invalid value for conversion")

print()

# TypeError
print("Example 3: TypeError")

try:
    result = "5" + 5
except TypeError:
    print("Error: Cannot add string and integer")

print()

# IndexError
print("Example 4: IndexError")

try:
    my_list = [1, 2, 3]
    print(my_list[10])
except IndexError:
    print("Error: Index out of range")

print()

# KeyError
print("Example 5: KeyError")

try:
    my_dict = {"name": "Alice", "age": 25}
    print(my_dict["email"])
except KeyError:
    print("Error: Key not found in dictionary")

print()

#==================================================================================
# MULTIPLE EXCEPT BLOCKS
#==================================================================================
"""
NOTES:
- Can have multiple except blocks
- Each handles different exception type
- First matching except block executes
- Allows different handling for different errors
"""

print("--- MULTIPLE EXCEPT BLOCKS ---")

def divide_numbers(a, b):
    try:
        result = a / b
        print(f"{a} / {b} = {result}")
    except ZeroDivisionError:
        print("Error: Cannot divide by zero")
    except TypeError:
        print("Error: Please provide numbers only")

print("Test 1:")
divide_numbers(10, 2)

print("\nTest 2:")
divide_numbers(10, 0)

print("\nTest 3:")
divide_numbers(10, "5")

print()

# Another example
print("List access example:")

def get_item(my_list, index):
    try:
        item = my_list[index]
        print(f"Item at index {index}: {item}")
    except IndexError:
        print(f"Error: Index {index} is out of range")
    except TypeError:
        print("Error: Index must be an integer")

numbers = [10, 20, 30, 40]
print(f"List: {numbers}")

get_item(numbers, 2)
get_item(numbers, 10)
get_item(numbers, "2")

print()

#==================================================================================
# HANDLING MULTIPLE EXCEPTIONS IN ONE BLOCK
#==================================================================================
"""
NOTES:
- Can catch multiple exceptions in single except
- Use tuple of exception types
- Same handling for multiple errors
- Reduces code duplication
"""

print("--- MULTIPLE EXCEPTIONS IN ONE BLOCK ---")

def calculate(a, b, operation):
    try:
        if operation == "divide":
            result = a / b
        elif operation == "add":
            result = a + b
        else:
            result = "Unknown operation"
        print(f"Result: {result}")
    except (ZeroDivisionError, TypeError, ValueError):
        print("Error: Invalid operation or values")

calculate(10, 2, "divide")
calculate(10, 0, "divide")
calculate(10, "5", "add")

print()

#==================================================================================
# EXCEPTION WITH VARIABLE (ACCESSING ERROR MESSAGE)
#==================================================================================
"""
NOTES:
- Use 'as' keyword to store exception object
- Can access error message and details
- Useful for debugging and logging
"""

print("--- ACCESSING ERROR MESSAGE ---")

try:
    number = int("hello")
except ValueError as e:
    print(f"Error occurred: {e}")

print()

try:
    result = 10 / 0
except ZeroDivisionError as error:
    print(f"Division error: {error}")

print()

# Example with list
try:
    my_list = [1, 2, 3]
    print(my_list[10])
except IndexError as e:
    print(f"Index error details: {e}")

print()

#==================================================================================
# TRY-EXCEPT-ELSE
#==================================================================================
"""
NOTES:
- else block executes if NO exception occurs
- Runs only when try block succeeds
- Code in else doesn't need exception handling
- Useful for code that depends on try block success
"""

print("--- TRY-EXCEPT-ELSE ---")

def divide_with_else(a, b):
    try:
        result = a / b
    except ZeroDivisionError:
        print("Error: Cannot divide by zero")
    else:
        print(f"Division successful: {a} / {b} = {result}")
        print("Calculation completed without errors")

print("Test 1:")
divide_with_else(10, 2)

print("\nTest 2:")
divide_with_else(10, 0)

print()

# Another example
print("File processing example:")

def process_number(value):
    try:
        number = int(value)
    except ValueError:
        print(f"Error: '{value}' is not a valid number")
    else:
        print(f"Successfully converted: {number}")
        print(f"Square: {number ** 2}")

process_number("10")
print()
process_number("abc")

print()

#==================================================================================
# TRY-EXCEPT-FINALLY
#==================================================================================
"""
NOTES:
- finally block ALWAYS executes
- Runs whether exception occurs or not
- Used for cleanup operations
- Useful for closing files, connections, etc.
"""

print("--- TRY-EXCEPT-FINALLY ---")

def divide_with_finally(a, b):
    try:
        result = a / b
        return result
    except ZeroDivisionError:
        print("Error: Division by zero")
    finally:
        print("Finally block always executes")
        print("Cleanup completed\n")

print("Test 1 (Success):")
divide_with_finally(10, 2)

print("Test 2 (Error):")
divide_with_finally(10, 0)

# Practical example
print("Resource management example:")

def open_file_simulation(filename):
    try:
        print(f"Opening file: {filename}")
        if filename == "error.txt":
            raise FileNotFoundError("File not found")
        print("Processing file...")
    except FileNotFoundError as e:
        print(f"Error: {e}")
    finally:
        print("Closing file (cleanup)")
        print()

open_file_simulation("data.txt")
open_file_simulation("error.txt")

#==================================================================================
# TRY-EXCEPT-ELSE-FINALLY (COMPLETE)
#==================================================================================
"""
NOTES:
- Can combine all four blocks
- Order: try -> except -> else -> finally
- else runs if no exception
- finally always runs
"""

print("--- COMPLETE TRY-EXCEPT-ELSE-FINALLY ---")

def complete_example(a, b):
    print(f"Attempting: {a} / {b}")
    
    try:
        result = a / b
    except ZeroDivisionError:
        print("Exception: Cannot divide by zero")
    else:
        print(f"Success: Result = {result}")
    finally:
        print("Cleanup: Operation completed\n")

complete_example(10, 2)
complete_example(10, 0)

#==================================================================================
# RAISING EXCEPTIONS
#==================================================================================
# """
# NOTES:
# - raise keyword manually raises exception
# - Useful for custom validation
# - Can raise built-in or custom exceptions
# - Stops program flow like normal exception
# """

# print("--- RAISING EXCEPTIONS ---")

# def check_age(age):
#     if age < 0:
#         raise ValueError("Age cannot be negative")
#     elif age < 18:
#         print("Minor")
#     else:
#         print("Adult")

# print("Test 1:")
# try:
#     check_age(25)
# except ValueError as e:
#     print(f"Error: {e}")

# print("\nTest 2:")
# try:
#     check_age(-5)
# except ValueError as e:
#     print(f"Error: {e}")

# print()

# # Another example
# def withdraw_money(balance, amount):
#     if amount <= 0:
#         raise ValueError("Amount must be positive")
#     if amount > balance:
#         raise ValueError("Insufficient balance")
#     return balance - amount

# print("Withdrawal example:")
# try:
#     new_balance = withdraw_money(1000, 500)
#     print(f"Withdrawal successful. New balance: {new_balance}")
# except ValueError as e:
#     print(f"Transaction failed: {e}")

# print()

# try:
#     new_balance = withdraw_money(1000, 1500)
#     print(f"Withdrawal successful. New balance: {new_balance}")
# except ValueError as e:
#     print(f"Transaction failed: {e}")

# print()

#==================================================================================
# NESTED TRY-EXCEPT
#==================================================================================
"""
NOTES:
- try-except blocks inside other try-except blocks
- Provides multiple levels of error handling
- Inner exceptions caught first
- Outer exceptions catch broader errors
"""

print("--- NESTED TRY-EXCEPT ---")

def nested_example():
    try:
        print("Outer try block")
        
        try:
            print("Inner try block")
            result = 10 / 0
        except ZeroDivisionError:
            print("Inner except: Caught division by zero")
        
        print("After inner try-except")
        number = int("abc")
        
    except ValueError:
        print("Outer except: Caught value error")

nested_example()

print()

#==================================================================================
# COMMON EXCEPTION TYPES
#==================================================================================
"""
NOTES:
- ZeroDivisionError: Division by zero
- ValueError: Invalid value for operation
- TypeError: Wrong type for operation
- IndexError: Index out of range
- KeyError: Dictionary key not found
- FileNotFoundError: File doesn't exist
- AttributeError: Attribute doesn't exist
- NameError: Variable not defined
"""

print("--- COMMON EXCEPTION TYPES ---")

# ZeroDivisionError
print("1. ZeroDivisionError:")
try:
    x = 5 / 0
except ZeroDivisionError:
    print("   Cannot divide by zero\n")

# ValueError
print("2. ValueError:")
try:
    num = int("not_a_number")
except ValueError:
    print("   Invalid conversion\n")

# TypeError
print("3. TypeError:")
try:
    result = "text" + 5
except TypeError:
    print("   Cannot add string and integer\n")

# IndexError
print("4. IndexError:")
try:
    lst = [1, 2, 3]
    item = lst[10]
except IndexError:
    print("   Index out of range\n")

# KeyError
print("5. KeyError:")
try:
    dct = {"name": "Alice"}
    value = dct["age"]
except KeyError:
    print("   Key not found\n")

# AttributeError
print("6. AttributeError:")
try:
    text = "hello"
    text.append("world")
except AttributeError:
    print("   Strings don't have append method\n")

# NameError
print("7. NameError:")
try:
    print(undefined_variable)
except NameError:
    print("   Variable not defined\n")

#==================================================================================
# REAL-LIFE EXCEPTION HANDLING EXAMPLES
#==================================================================================

# Example 1: Safe Division Calculator
print("--- EXAMPLE 1: SAFE DIVISION CALCULATOR ---")

def safe_divide(a, b):
    """Safely divide two numbers with error handling."""
    try:
        result = a / b
        return result
    except ZeroDivisionError:
        return "Error: Cannot divide by zero"
    except TypeError:
        return "Error: Both inputs must be numbers"

print(f"10 / 2 = {safe_divide(10, 2)}")
print(f"10 / 0 = {safe_divide(10, 0)}")
print(f"10 / '5' = {safe_divide(10, '5')}")

print()

# Example 2: User Input Validation
print("--- EXAMPLE 2: USER INPUT VALIDATION ---")

def get_valid_age(age_input):
    """Validate and return age."""
    try:
        age = int(age_input)
        if age < 0:
            return None, "Age cannot be negative"
        if age > 150:
            return None, "Invalid age"
        return age, "Valid age"
    except ValueError:
        return None, "Please enter a valid number"

# Test different inputs
test_inputs = ["25", "-5", "abc", "200"]
for inp in test_inputs:
    age, message = get_valid_age(inp)
    print(f"Input: '{inp}' -> {message} (Age: {age})")

print()

# Example 3: List Operations Safety
print("--- EXAMPLE 3: SAFE LIST ACCESS ---")

def safe_get_item(lst, index):
    """Safely get item from list."""
    try:
        return lst[index], "Success"
    except IndexError:
        return None, f"Index {index} out of range (list size: {len(lst)})"
    except TypeError:
        return None, "Index must be an integer"

numbers = [10, 20, 30, 40, 50]
print(f"List: {numbers}")

test_indices = [2, 10, "2", -1]
for idx in test_indices:
    item, status = safe_get_item(numbers, idx)
    print(f"Index {idx}: {status} -> Item: {item}")

print()

# Example 4: Dictionary Operations
print("--- EXAMPLE 4: SAFE DICTIONARY ACCESS ---")

def get_user_info(users, user_id):
    """Safely get user information."""
    try:
        user = users[user_id]
        return f"User found: {user}"
    except KeyError:
        return f"User ID {user_id} not found"

users_db = {
    101: {"name": "Alice", "age": 25},
    102: {"name": "Bob", "age": 30},
    103: {"name": "Charlie", "age": 28}
}

print(get_user_info(users_db, 101))
print(get_user_info(users_db, 999))

print()

# Example 5: Temperature Converter with Validation
print("--- EXAMPLE 5: TEMPERATURE CONVERTER ---")

def convert_temperature(value, from_unit, to_unit):
    """Convert temperature between Celsius and Fahrenheit."""
    try:
        temp = float(value)
        
        if from_unit == "C" and to_unit == "F":
            result = (temp * 9/5) + 32
            return f"{temp}°C = {result}°F"
        elif from_unit == "F" and to_unit == "C":
            result = (temp - 32) * 5/9
            return f"{temp}°F = {result:.1f}°C"
        else:
            return "Invalid units (use 'C' or 'F')"
            
    except ValueError:
        return "Invalid temperature value"

print(convert_temperature("25", "C", "F"))
print(convert_temperature("77", "F", "C"))
print(convert_temperature("abc", "C", "F"))
print(convert_temperature("25", "C", "X"))

print()

# Example 6: Bank Account Operations
print("--- EXAMPLE 6: BANK ACCOUNT OPERATIONS ---")

class BankAccount:
    def __init__(self, balance):
        self.balance = balance
    
    def withdraw(self, amount):
        """Withdraw money with error handling."""
        try:
            amount = float(amount)
            
            if amount <= 0:
                raise ValueError("Amount must be positive")
            if amount > self.balance:
                raise ValueError("Insufficient balance")
            
            self.balance -= amount
            return True, f"Withdrawal successful. New balance: ${self.balance:.2f}"
            
        except ValueError as e:
            return False, f"Error: {e}"
        except TypeError:
            return False, "Error: Invalid amount type"

account = BankAccount(1000)
print(f"Initial balance: ${account.balance}")

transactions = [200, 1500, -50, "abc", 300]
for amount in transactions:
    success, message = account.withdraw(amount)
    print(f"Withdraw {amount}: {message}")

print()

# Example 7: File Reading Simulation
print("--- EXAMPLE 7: FILE READING SIMULATION ---")

def read_file_safe(filename):
    """Simulate safe file reading."""
    try:
        # Simulating file operations
        if filename == "":
            raise ValueError("Filename cannot be empty")
        if not filename.endswith(".txt"):
            raise ValueError("Only .txt files supported")
        if filename == "missing.txt":
            raise FileNotFoundError("File not found")
        
        return f"Successfully read: {filename}"
        
    except ValueError as e:
        return f"Error: {e}"
    except FileNotFoundError as e:
        return f"Error: {e}"
    finally:
        print(f"  Cleanup: Closed file operations for '{filename}'")

files = ["data.txt", "missing.txt", "file.pdf", ""]
for file in files:
    print(f"\nAttempting: '{file}'")
    result = read_file_safe(file)
    print(f"  Result: {result}")

print()

# Example 8: Login System with Attempts
print("--- EXAMPLE 8: LOGIN SYSTEM ---")

def login_system(username, password, max_attempts=3):
    """Login system with attempt limit."""
    correct_username = "admin"
    correct_password = "secure123"
    
    attempts = 0
    
    try:
        if not username or not password:
            raise ValueError("Username and password required")
        
        attempts += 1
        
        if username != correct_username:
            raise ValueError("Invalid username")
        if password != correct_password:
            raise ValueError("Invalid password")
        
        return True, "Login successful"
        
    except ValueError as e:
        return False, f"Login failed: {e}"

# Test different credentials
credentials = [
    ("admin", "secure123"),
    ("admin", "wrong"),
    ("", "password"),
    ("user", "pass")
]

for user, pwd in credentials:
    success, message = login_system(user, pwd)
    print(f"User: '{user}' -> {message}")

print()

# Example 9: Shopping Cart with Validation
print("--- EXAMPLE 9: SHOPPING CART VALIDATION ---")

def add_to_cart(cart, item, quantity, price):
    """Add item to cart with validation."""
    try:
        quantity = int(quantity)
        price = float(price)
        
        if quantity <= 0:
            raise ValueError("Quantity must be positive")
        if price < 0:
            raise ValueError("Price cannot be negative")
        if not item or item.strip() == "":
            raise ValueError("Item name required")
        
        cart.append({
            "item": item,
            "quantity": quantity,
            "price": price,
            "total": quantity * price
        })
        return True, f"Added {quantity}x {item} to cart"
        
    except ValueError as e:
        return False, f"Error: {e}"
    except TypeError:
        return False, "Error: Invalid data type"

shopping_cart = []
items_to_add = [
    ("Laptop", 1, 999.99),
    ("Mouse", -2, 24.99),
    ("", 1, 10),
    ("Keyboard", "two", 79.99)
]

for item, qty, price in items_to_add:
    success, message = add_to_cart(shopping_cart, item, qty, price)
    print(message)

print(f"\nCart items: {len(shopping_cart)}")
for item in shopping_cart:
    print(f"  {item['item']}: {item['quantity']} × ${item['price']} = ${item['total']}")

print()

# Example 10: Grade Calculator with Validation
print("--- EXAMPLE 10: GRADE CALCULATOR ---")

def calculate_grade_safe(marks_list):
    """Calculate grade with comprehensive error handling."""
    try:
        if not marks_list:
            raise ValueError("Marks list cannot be empty")
        
        # Convert all to float and validate
        marks = []
        for mark in marks_list:
            m = float(mark)
            if m < 0 or m > 100:
                raise ValueError(f"Invalid mark: {m} (must be 0-100)")
            marks.append(m)
        
        average = sum(marks) / len(marks)
        
        if average >= 90:
            grade = "A+"
        elif average >= 80:
            grade = "A"
        elif average >= 70:
            grade = "B"
        elif average >= 60:
            grade = "C"
        else:
            grade = "F"
        
        return {
            "success": True,
            "average": average,
            "grade": grade,
            "message": f"Average: {average:.2f}, Grade: {grade}"
        }
        
    except ValueError as e:
        return {
            "success": False,
            "message": f"Error: {e}"
        }
    except TypeError:
        return {
            "success": False,
            "message": "Error: All marks must be numbers"
        }

# Test different mark sets
test_marks = [
    [85, 90, 88, 92],
    [75, 80, 150],
    [],
    [90, "abc", 85]
]

for i, marks in enumerate(test_marks, 1):
    print(f"Test {i}: {marks}")
    result = calculate_grade_safe(marks)
    print(f"  {result['message']}\n")

print("="*80)
print("END OF EXCEPTION HANDLING TUTORIAL")
print("="*80)