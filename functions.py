#==================================================================================
# FUNCTIONS IN PYTHON
#==================================================================================
"""
NOTES:
- Function is a block of reusable code
- Functions perform a specific task
- Functions help organize code and avoid repetition
- Defined using 'def' keyword
- Called by using function name followed by ()
"""

#==================================================================================
# DEFINING AND CALLING A FUNCTION
#==================================================================================
"""
NOTES:
- def keyword defines a function
- Function name should be descriptive and lowercase
- Parentheses () are required
- Colon : starts the function body
- Function body must be indented
- Call function using function_name()
"""

# Basic function
def greet():
    print("Hello, World!")

print("--- BASIC FUNCTION ---")
print("Calling greet():")
greet()

# Function with multiple statements
def welcome():
    print("Welcome to Python!")
    print("Let's learn functions")
    print("Functions are awesome")

print("\nCalling welcome():")
welcome()

# Calling function multiple times
print("\nCalling greet() three times:")
greet()
greet()
greet()

#==================================================================================
# FUNCTION WITH PARAMETERS
#==================================================================================
"""
NOTES:
- Parameters are variables in function definition
- Parameters receive values when function is called
- Multiple parameters separated by commas
- Parameters are local to the function
"""

# Function with one parameter
def greet_person(name):
    print(f"Hello, {name}!")

print("\n--- FUNCTION WITH PARAMETERS ---")
greet_person("Alice")
greet_person("Bob")
greet_person("Charlie")

# Function with multiple parameters
def add_numbers(a, b):
    result = a + b
    print(f"{a} + {b} = {result}")

print("\nAdding numbers:")
add_numbers(5, 3)
add_numbers(10, 20)
add_numbers(100, 250)

# Another example
def introduce(name, age):
    print(f"My name is {name} and I am {age} years old")

print("\nIntroductions:")
introduce("Alice", 25)
introduce("Bob", 30)

# Three parameters
def calculate_rectangle(length, width, unit):
    area = length * width
    print(f"Rectangle: {length}{unit} × {width}{unit}")
    print(f"Area: {area} square {unit}")

print("\nRectangle calculations:")
calculate_rectangle(5, 3, "cm")

#==================================================================================
# ARGUMENTS VS PARAMETERS
#==================================================================================
"""
NOTES:
- Parameter: variable in function definition
- Argument: actual value passed to function
- Example: def func(parameter): func(argument)
"""

# Example demonstrating the difference
def display_info(name, age):  # name and age are parameters
    print(f"Name: {name}, Age: {age}")

print("\n--- ARGUMENTS VS PARAMETERS ---")
display_info("Alice", 25)  # "Alice" and 25 are arguments

#==================================================================================
# RETURN STATEMENT
#==================================================================================
"""
NOTES:
- return sends a value back to the caller
- Function execution stops at return
- Without return, function returns None
- Can return any data type
"""

# Function with return
def add(a, b):
    result = a + b
    return result

print("\n--- RETURN STATEMENT ---")
sum_result = add(5, 3)
print(f"5 + 3 = {sum_result}")

total = add(10, 20)
print(f"10 + 20 = {total}")

# Using return value in expression
answer = add(5, 7) + add(10, 15)
print(f"(5 + 7) + (10 + 15) = {answer}")

# Function without return (returns None)
def print_message(msg):
    print(msg)

print("\nFunction without return:")
result = print_message("Hello")
print(f"Return value: {result}")

# Return different data types
def get_square(num):
    return num * num

def get_name():
    return "Alice"

def get_numbers():
    return [1, 2, 3, 4, 5]

print("\nReturning different types:")
print(f"Square of 5: {get_square(5)}")
print(f"Name: {get_name()}")
print(f"Numbers: {get_numbers()}")

#==================================================================================
# RETURN MULTIPLE VALUES
#==================================================================================
"""
NOTES:
- Python functions can return multiple values
- Multiple values returned as tuple
- Can unpack multiple return values
"""

# Returning multiple values
def get_min_max(numbers):
    minimum = min(numbers)
    maximum = max(numbers)
    return minimum, maximum

print("\n--- RETURNING MULTIPLE VALUES ---")
nums = [5, 2, 9, 1, 7]
print(f"Numbers: {nums}")

min_val, max_val = get_min_max(nums)
print(f"Minimum: {min_val}")
print(f"Maximum: {max_val}")

# Another example
def divide_with_remainder(dividend, divisor):
    quotient = dividend // divisor
    remainder = dividend % divisor
    return quotient, remainder

print("\n17 divided by 5:")
q, r = divide_with_remainder(17, 5)
print(f"Quotient: {q}")
print(f"Remainder: {r}")

# Three return values
def get_statistics(numbers):
    total = sum(numbers)
    count = len(numbers)
    average = total / count
    return total, count, average

data = [10, 20, 30, 40, 50]
print(f"\nData: {data}")
sum_val, count_val, avg_val = get_statistics(data)
print(f"Sum: {sum_val}, Count: {count_val}, Average: {avg_val}")

#==================================================================================
# DEFAULT PARAMETERS
#==================================================================================
"""
NOTES:
- Default parameters have default values
- Used if argument not provided
- Must come after non-default parameters
- Makes functions more flexible
"""

# Function with default parameter
def greet_with_message(name, message="Hello"):
    print(f"{message}, {name}!")

print("\n--- DEFAULT PARAMETERS ---")
greet_with_message("Alice")
greet_with_message("Bob", "Good morning")
greet_with_message("Charlie", "Welcome")

# Multiple default parameters
def make_profile(name, age, city="Unknown", country="Unknown"):
    print(f"Name: {name}")
    print(f"Age: {age}")
    print(f"City: {city}")
    print(f"Country: {country}")
    print()

print("Profile 1:")
make_profile("Alice", 25)

print("Profile 2:")
make_profile("Bob", 30, "New York")

print("Profile 3:")
make_profile("Charlie", 28, "London", "UK")

# Default parameter with calculations
def calculate_power(base, exponent=2):
    result = base ** exponent
    return result

print("Power calculations:")
print(f"5^2 = {calculate_power(5)}")
print(f"5^3 = {calculate_power(5, 3)}")
print(f"2^4 = {calculate_power(2, 4)}")

#==================================================================================
# KEYWORD ARGUMENTS
#==================================================================================
"""
NOTES:
- Arguments passed by parameter name
- Order doesn't matter with keyword arguments
- Can mix positional and keyword arguments
- Keyword arguments must come after positional
"""

# Using keyword arguments
def describe_pet(animal, name, age):
    print(f"I have a {animal}")
    print(f"Name: {name}")
    print(f"Age: {age}")
    print()

print("\n--- KEYWORD ARGUMENTS ---")
print("Using positional arguments:")
describe_pet("dog", "Buddy", 3)

print("Using keyword arguments:")
describe_pet(animal="cat", name="Whiskers", age=2)

print("Keyword arguments in different order:")
describe_pet(name="Max", age=5, animal="dog")

print("Mix of positional and keyword:")
describe_pet("bird", name="Tweety", age=1)

#==================================================================================
# VARIABLE SCOPE
#==================================================================================
"""
NOTES:
- Local variables: created inside function
- Global variables: created outside function
- Local variables only accessible inside function
- Global variables accessible everywhere
"""

# Local vs Global scope
global_var = "I am global"

def show_scope():
    local_var = "I am local"
    print(f"Inside function - Global: {global_var}")
    print(f"Inside function - Local: {local_var}")

print("\n--- VARIABLE SCOPE ---")
show_scope()
print(f"Outside function - Global: {global_var}")
# print(local_var)  # NameError: local_var not accessible outside

# Local variable shadows global
message = "Global message"

def test_scope():
    message = "Local message"
    print(f"Inside function: {message}")

print("\nVariable shadowing:")
test_scope()
print(f"Outside function: {message}")

# Parameter is also local
def multiply(x):
    x = x * 2
    print(f"Inside function x: {x}")

print("\nParameter scope:")
x = 10
print(f"Before function x: {x}")
multiply(x)
print(f"After function x: {x}")

#==================================================================================
# GLOBAL KEYWORD
#==================================================================================
"""
NOTES:
- global keyword modifies global variable inside function
- Without global, assignment creates local variable
- Use sparingly - better to use return values
"""

# Using global keyword
counter = 0

def increment():
    global counter
    counter += 1
    print(f"Counter inside function: {counter}")

print("\n--- GLOBAL KEYWORD ---")
print(f"Counter before: {counter}")
increment()
print(f"Counter after first call: {counter}")
increment()
print(f"Counter after second call: {counter}")

# Without global keyword
value = 10

def try_modify():
    value = 20  # Creates local variable
    print(f"Inside function: {value}")

print("\nWithout global keyword:")
print(f"Before function: {value}")
try_modify()
print(f"After function: {value}")

# #==================================================================================
# # DOCSTRINGS
# #==================================================================================
# """
# NOTES:
# - Docstrings document what function does
# - First statement in function
# - Enclosed in triple quotes
# - Accessible via __doc__ attribute
# - Good practice for code documentation
# """

# # Function with docstring
# def calculate_area(length, width):
#     """
#     Calculate the area of a rectangle.
    
#     Parameters:
#     length: length of rectangle
#     width: width of rectangle
    
#     Returns:
#     area of rectangle
#     """
#     return length * width

# print("\n--- DOCSTRINGS ---")
# print("Function docstring:")
# print(calculate_area.__doc__)

# result = calculate_area(5, 3)
# print(f"\nArea: {result}")

# # Another example
# def greet_user(name):
#     """Greet the user with their name."""
#     return f"Hello, {name}!"

# print("\nShort docstring:")
# print(greet_user.__doc__)

#==================================================================================
# FUNCTIONS CALLING OTHER FUNCTIONS
#==================================================================================
"""
NOTES:
- Functions can call other functions
- Helps break complex problems into smaller parts
- Makes code more organized and reusable
"""

# Functions calling functions
def get_formatted_name(first, last):
    """Return formatted full name."""
    full_name = f"{first} {last}"
    return full_name.title()

def greet_user_formally(first, last):
    """Greet user with formatted name."""
    name = get_formatted_name(first, last)
    print(f"Good morning, {name}!")

print("\n--- FUNCTIONS CALLING FUNCTIONS ---")
greet_user_formally("john", "doe")
greet_user_formally("alice", "smith")

# More complex example
def get_square(num):
    """Return square of number."""
    return num * num

def get_sum_of_squares(a, b):
    """Return sum of squares of two numbers."""
    square_a = get_square(a)
    square_b = get_square(b)
    return square_a + square_b

print(f"\nSum of squares of 3 and 4: {get_sum_of_squares(3, 4)}")

#==================================================================================
# RECURSIVE FUNCTIONS (BASIC)
#==================================================================================
"""
NOTES:
- Recursive function calls itself
- Must have base case to stop recursion
- Useful for certain mathematical problems
- Be careful of infinite recursion
"""

# Factorial using recursion
def factorial(n):
    """Calculate factorial using recursion."""
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)

print("\n--- RECURSIVE FUNCTIONS ---")
print(f"Factorial of 5: {factorial(5)}")
print(f"Factorial of 3: {factorial(3)}")

# Countdown using recursion
def countdown(n):
    """Countdown from n to 1."""
    if n <= 0:
        print("Done!")
    else:
        print(n)
        countdown(n - 1)

print("\nCountdown from 5:")
countdown(5)

#==================================================================================
# LAMBDA FUNCTIONS (ANONYMOUS FUNCTIONS)
#==================================================================================
"""
NOTES:
- Lambda functions are small anonymous functions
- Defined using lambda keyword
- Can have multiple parameters but only one expression
- Useful for short, simple operations
"""

# Basic lambda function
square = lambda x: x * x

print("\n--- LAMBDA FUNCTIONS ---")
print(f"Square of 5: {square(5)}")
print(f"Square of 7: {square(7)}")

# Lambda with two parameters
add = lambda a, b: a + b
print(f"\n3 + 4 = {add(3, 4)}")

multiply = lambda x, y: x * y
print(f"5 × 6 = {multiply(5, 6)}")

# Lambda with three parameters
calculate = lambda a, b, c: (a + b) * c
print(f"(2 + 3) × 4 = {calculate(2, 3, 4)}")

# # Using lambda in sorted()
# students = [("Alice", 85), ("Bob", 92), ("Charlie", 78)]
# print("\nOriginal list:", students)

# sorted_students = sorted(students, key=lambda x: x[1], reverse=True)
# print("Sorted by score:", sorted_students)

#==================================================================================
# BUILT-IN FUNCTIONS REVIEW
#==================================================================================
"""
NOTES:
- Python provides many built-in functions
- Already covered: print(), len(), sum(), max(), min(), etc.
- Here are some useful ones with functions
"""

# map() - applies function to each item
def square_num(x):
    return x * x

print("\n--- BUILT-IN FUNCTIONS ---")
numbers = [1, 2, 3, 4, 5]
print(f"Numbers: {numbers}")

squared = list(map(square_num, numbers))
print(f"Squared: {squared}")

# map() with lambda
doubled = list(map(lambda x: x * 2, numbers))
print(f"Doubled: {doubled}")

# Combining map() and filter()
mul_of_3 = list(filter(lambda y: y % 3 == 0, list(map(lambda x: x * 2, numbers))))
print(f"Multiple of 3: {mul_of_3}")

# filter() - filters items based on condition
def is_even(x):
    return x % 2 == 0

print("\nFiltering even numbers:")
evens = list(filter(is_even, numbers))
print(f"Even numbers: {evens}")

# filter() with lambda
odds = list(filter(lambda x: x % 2 != 0, numbers))
print(f"Odd numbers: {odds}")

#==================================================================================
# REAL-LIFE FUNCTION EXAMPLES
#==================================================================================

# Example 1: Calculator Functions
print("\n--- EXAMPLE 1: CALCULATOR ---")

def add(a, b):
    """Add two numbers."""
    return a + b

def subtract(a, b):
    """Subtract b from a."""
    return a - b

def multiply(a, b):
    """Multiply two numbers."""
    return a * b

def divide(a, b):
    """Divide a by b."""
    if b == 0:
        return "Error: Division by zero"
    return a / b

print(f"10 + 5 = {add(10, 5)}")
print(f"10 - 5 = {subtract(10, 5)}")
print(f"10 × 5 = {multiply(10, 5)}")
print(f"10 ÷ 5 = {divide(10, 5)}")
print(f"10 ÷ 0 = {divide(10, 0)}")

# Example 2: Temperature Converter
print("\n--- EXAMPLE 2: TEMPERATURE CONVERTER ---")

def celsius_to_fahrenheit(celsius):
    """Convert Celsius to Fahrenheit."""
    fahrenheit = (celsius * 9/5) + 32
    return fahrenheit

def fahrenheit_to_celsius(fahrenheit):
    """Convert Fahrenheit to Celsius."""
    celsius = (fahrenheit - 32) * 5/9
    return celsius

temp_c = 25
temp_f = celsius_to_fahrenheit(temp_c)
print(f"{temp_c}°C = {temp_f}°F")

temp_f2 = 77
temp_c2 = fahrenheit_to_celsius(temp_f2)
print(f"{temp_f2}°F = {temp_c2:.1f}°C")

# Example 3: Grade Calculator
print("\n--- EXAMPLE 3: GRADE CALCULATOR ---")

def calculate_grade(marks):
    """Calculate grade based on marks."""
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
    
    return grade, average

student_marks = [85, 90, 88, 92, 87]
grade, avg = calculate_grade(student_marks)
print(f"Marks: {student_marks}")
print(f"Average: {avg:.2f}")
print(f"Grade: {grade}")

# Example 4: Password Validator
print("\n--- EXAMPLE 4: PASSWORD VALIDATOR ---")

def is_strong_password(password):
    """
    Check if password is strong.
    Strong password: length >= 8, has digit, has uppercase
    """
    if len(password) < 8:
        return False, "Password too short (minimum 8 characters)"
    
    has_digit = False
    has_upper = False
    
    for char in password:
        if char.isdigit():
            has_digit = True
        if char.isupper():
            has_upper = True
    
    if not has_digit:
        return False, "Password must contain at least one digit"
    if not has_upper:
        return False, "Password must contain at least one uppercase letter"
    
    return True, "Password is strong"

passwords = ["weak", "Strong123", "nodigits", "nocaps123"]
for pwd in passwords:
    is_strong, message = is_strong_password(pwd)
    print(f"'{pwd}': {message}")

# Example 5: Area Calculator
print("\n--- EXAMPLE 5: AREA CALCULATOR ---")

def calculate_circle_area(radius):
    """Calculate area of circle."""
    pi = 3.14159
    return pi * radius * radius

def calculate_rectangle_area(length, width):
    """Calculate area of rectangle."""
    return length * width

def calculate_triangle_area(base, height):
    """Calculate area of triangle."""
    return 0.5 * base * height

print(f"Circle (radius=5): {calculate_circle_area(5):.2f}")
print(f"Rectangle (10×5): {calculate_rectangle_area(10, 5)}")
print(f"Triangle (base=6, height=4): {calculate_triangle_area(6, 4)}")

# Example 6: List Operations
print("\n--- EXAMPLE 6: LIST OPERATIONS ---")

def get_even_numbers(numbers):
    """Return list of even numbers."""
    evens = []
    for num in numbers:
        if num % 2 == 0:
            evens.append(num)
    return evens

def get_sum_and_average(numbers):
    """Return sum and average of numbers."""
    total = sum(numbers)
    avg = total / len(numbers)
    return total, avg

numbers_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(f"Numbers: {numbers_list}")

evens_list = get_even_numbers(numbers_list)
print(f"Even numbers: {evens_list}")

total, average = get_sum_and_average(numbers_list)
print(f"Sum: {total}, Average: {average}")

# Example 7: String Formatter
print("\n--- EXAMPLE 7: STRING FORMATTER ---")

def format_name(first, last):
    """Format name as 'Last, First'."""
    return f"{last}, {first}"

def create_email(first, last, domain="company.com"):
    """Create email from name."""
    email = f"{first.lower()}.{last.lower()}@{domain}"
    return email

def create_username(first, last):
    """Create username from name."""
    username = (first[0] + last).lower()
    return username

first_name = "John"
last_name = "Doe"

print(f"Formatted name: {format_name(first_name, last_name)}")
print(f"Email: {create_email(first_name, last_name)}")
print(f"Username: {create_username(first_name, last_name)}")

# Example 8: Discount Calculator
print("\n--- EXAMPLE 8: DISCOUNT CALCULATOR ---")

def calculate_discount(price, discount_percent):
    """Calculate discounted price."""
    discount_amount = price * (discount_percent / 100)
    final_price = price - discount_amount
    return final_price, discount_amount

def apply_seasonal_discount(price, is_member=False):
    """Apply seasonal discount based on membership."""
    if is_member:
        discount = 20
    else:
        discount = 10
    
    return calculate_discount(price, discount)

original_price = 100
final, saved = calculate_discount(original_price, 15)
print(f"Original: ${original_price}")
print(f"Discount: 15%")
print(f"You save: ${saved:.2f}")
print(f"Final price: ${final:.2f}")

print("\nSeasonal discount:")
member_price, member_saved = apply_seasonal_discount(100, True)
print(f"Member: ${member_price:.2f} (saved ${member_saved:.2f})")

non_member_price, non_member_saved = apply_seasonal_discount(100, False)
print(f"Non-member: ${non_member_price:.2f} (saved ${non_member_saved:.2f})")

# Example 9: Prime Number Checker
print("\n--- EXAMPLE 9: PRIME NUMBER CHECKER ---")

def is_prime(number):
    """Check if number is prime."""
    if number < 2:
        return False
    
    for i in range(2, number):
        if number % i == 0:
            return False
    
    return True

def get_primes_up_to(n):
    """Get all prime numbers up to n."""
    primes = []
    for num in range(2, n + 1):
        if is_prime(num):
            primes.append(num)
    return primes

test_numbers = [2, 7, 10, 13, 15, 17]
print("Prime check:")
for num in test_numbers:
    if is_prime(num):
        print(f"{num} is prime")
    else:
        print(f"{num} is not prime")

print(f"\nPrimes up to 20: {get_primes_up_to(20)}")

# Example 10: Shopping Cart
print("\n--- EXAMPLE 10: SHOPPING CART ---")

def add_to_cart(cart, item, price):
    """Add item to shopping cart."""
    cart.append({"item": item, "price": price})
    return cart

def calculate_total(cart):
    """Calculate total price of items in cart."""
    total = 0
    for item in cart:
        total += item["price"]
    return total

def display_cart(cart):
    """Display all items in cart."""
    print("\nShopping Cart:")
    for i, item in enumerate(cart, 1):
        print(f"{i}. {item['item']}: ${item['price']:.2f}")

my_cart = []
my_cart = add_to_cart(my_cart, "Laptop", 999.99)
my_cart = add_to_cart(my_cart, "Mouse", 24.99)
my_cart = add_to_cart(my_cart, "Keyboard", 79.99)

display_cart(my_cart)
total_price = calculate_total(my_cart)
print(f"\nTotal: ${total_price:.2f}")
