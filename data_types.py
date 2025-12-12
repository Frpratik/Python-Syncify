"""
1. Numeric Types

int → integer numbers (10, -5, 0)

float → decimal numbers (3.14, -0.5)

complex → complex numbers (2 + 3j)

2. Text Type

str → string (text)

3. Boolean Type

bool → True or False

4. Sequence Types

list → ordered, changeable list, []

tuple → ordered, unchangeable list, ()

5. Set Types

set → unordered unique values {}

6. Mapping Type

dict → key–value pairs {k:v}

"""

"""
1. Numeric Types

int → integer numbers (10, -5, 0)

float → decimal numbers (3.14, -0.5)

complex → complex numbers (2 + 3j)

2. Boolean Type

bool → True or False

3. Text Type

str → string (text)

4. Sequence Types

list → ordered, changeable list

tuple → ordered, unchangeable list

5. Set Types

set → unordered unique values

6. Mapping Type

dict → key–value pairs

"""

# INT (INTEGER) DATA TYPE IN PYTHON

# int means: whole number without decimal point

a = 10
b = -20
c = 0

print(a, b, c)

# To check the data type 
print(type(a))   # <class 'int'>
print(type(b))   # <class 'int'>
print(type(c))   # <class 'int'>


# ----- BASIC ARITHMETIC OPERATIONS WITH int ----- #

a = 10
b = 3

# Addition
print(a + b)   # 13

# Subtraction
print(a - b)   # 7

# Multiplication
print(a * b)   # 30

# Division – / vs //
print(a / b)   # 3.3333333333 (normal division, result is float)
print(a // b)  # 3            (floor division, result is int)

# / → normal division (can give decimal)
# // → “cut off” the decimal part (floor division)


# Remainder (Modulo)
print(a % b)   # 1

# % gives remainder after division.
# Example: 10 / 3 is 3 with remainder 1 → % gives 1.


# Power (Exponent)
print(a ** b)  # 10 ** 3 = 1000

# a ** b means “a to the power b”.


# ----- COMPARISON OPERATORS WITH int ----- #

# Comparison always returns True or False (returns boolean val).

x = 10
y = 20

print(x == y)   # False
print(x != y)   # True
print(x > y)    # False
print(x < y)    # True
print(x >= 10)  # True
print(y <= 20)  # True


# ----- TYPE CONVERSION (CASTING) WITH int ----- #

# float -> int (cuts off decimal part)
f1 = 3.9
f2 = 5.1

print(int(f1))   # 3  (not 4, decimal part is removed)
print(int(f2))   # 5

# string -> int (string must be a whole number)
s1 = "10"
s2 = "20"

print(int(s1))   # 10
print(int(s2))   # 250

# Invalid conversions (will give error if you try)
# int("10.5")    # ValueError (string has decimal)
# int("abc")     # ValueError

#==================================================================================

# FLOAT DATA TYPE IN PYTHON

# Float means: number with decimal point

x = 3.14
y = -2.5
z = 0.0

print(x, y, z)

# To check the data type
print(type(x))   # <class 'float'>
print(type(y))   # <class 'float'>
print(type(z))   # <class 'float'>


# Basic arithmetic operations with float

a = 5.5
b = 2.0

# Addition
print(a + b)   # 7.5

# Subtraction
print(a - b)   # 3.5

# Multiplication
print(a * b)   # 11.0

# Division
print(a / b)   # 2.75 (normal division, result is float)

# Floor division //
print(a // b)  # 2.0 (cuts off decimal part, result is still float)

# Remainder (Modulo)
print(a % b)   # 1.5

# Power (Exponent)
print(a ** b)  # 5.5 ** 2.0 = 30.25


# Mixing int and float

p = 10      # int
q = 3.5     # float

print(p + q)   # 13.5 (float)
print(p * q)   # 35.0 (float)
print(p / q)   # 2.857142857142857 (float)


# Comparison operators with float

m = 10.5
n = 20.0

print(m == n)    # False
print(m != n)    # True
print(m > n)     # False
print(m < n)     # True
print(m >= 10.5) # True
print(n <= 20.0) # True


# Type conversion (casting) with float

# int -> float
num_int = 5
num_float = float(num_int)
print(num_int, type(num_int))       # 5 <class 'int'>
print(num_float, type(num_float))   # 5.0 <class 'float'>

# string -> float
s1 = "3.5"
s2 = "10"
print(float(s1))    # 3.5
print(float(s2))    # 10.0

# Invalid conversions (will give error if you try)
# float("abc")     # ValueError
# float("10a")     # ValueError


# ----- BUILT-IN FUNCTIONS AND USEFUL THINGS WITH FLOAT ----- #

# type() - to check the data type
val = 4.75
print(type(val))    # <class 'float'>

# float() - to convert other types to float
print(float(7))         # 7.0 (int -> float)
print(float("2.25"))    # 2.25 (string -> float)

# round() - to round float values

pi = 3.14159265

print(round(pi))       # 3      (rounded to nearest integer)
print(round(pi, 2))    # 3.14   (2 decimal places)
print(round(pi, 3))    # 3.142  (3 decimal places)

# Example: floating-point precision issue
print(0.1 + 0.2)         # 0.30000000000000004 (small precision error)
print(round(0.1 + 0.2, 2))  # 0.3 (use round to clean it)

#==================================================================================

# COMPLEX NUMBERS (complex) IN PYTHON

# Complex number: a + bj
# a → real part (int or float)
# b → imaginary part (int or float)
# j → imaginary unit (√-1)

# Creating complex numbers

z1 = 2 + 3j       # real = 2, imaginary = 3
z2 = -1 - 4j
z3 = 5.0 + 0j     # real part float
z4 = 0 + 2j       # only imaginary

print(z1, z2, z3, z4)

# Check data type
print(type(z1))   # <class 'complex'>

# Accessing real and imaginary parts
print(z1.real)    # 2.0
print(z1.imag)    # 3.0

print(z2.real)    # -1.0
print(z2.imag)    # -4.0


# ----- BASIC OPERATIONS WITH COMPLEX NUMBERS ----- #

a = 2 + 3j
b = 1 - 4j

# Addition
print(a + b)    # (3-1j)

# Subtraction
print(a - b)    # (1+7j)

# Multiplication
print(a * b)    # (14-5j)

# Division
print(a / b)    # ( -0.5882352941176471 + 0.6470588235294118j ) approx


# Conjugate of a complex number
# For z = a + bj, conjugate is a - bj
z = 3 + 4j
print(z.conjugate())    # (3-4j)


# Magnitude (absolute value / modulus)
# |z| = √(a² + b²)
# In Python: use abs()
print(abs(z))   # 5.0  (because √(3² + 4²) = 5)


# Creating complex numbers using complex() function

# complex(real, imag) - Typecast/Type Conversion to complex number
c1 = complex(2, 3)      # 2 + 3j
c2 = complex(5, -1)     # 5 - 1j
c3 = complex(7)         # 7 + 0j
c4 = complex("2+3j")    # from string

print(c1, c2, c3, c4)
print(type(c4))         # <class 'complex'>


# Mixing with int and float

x = 5          # int
y = 2.5        # float
z = 3 + 4j     # complex

print(x + z)   # (8+4j)
print(y + z)   # (5.5+4j)

# Note: if you mix int/float with complex, result becomes complex


# Using complex numbers in simple examples

# Example 1: Electrical engineering (impedance)
r = 4          # resistance (real part)
x_react = 3    # reactance (imaginary part)
impedance = complex(r, x_react)   # 4 + 3j
print("Impedance:", impedance)

# Example 2: Distance from origin in complex plane
point = 3 + 4j
distance = abs(point)   # same as sqrt(3^2 + 4^2)
print("Distance from origin:", distance)  # 5.0

#==================================================================================

# STRING (str) - Text data

# Creating strings - Method 1: Double quotes
name = "John Doe"
city = "Mumbai"

# Creating strings - Method 2: Single quotes
message = 'Hello World'
quote = 'Python is awesome'

# Both work the same
print(name)
print(message)

# When to use which quotes?
# Use single quotes inside double quotes
sentence1 = "Python's syntax is easy"
print(sentence1)

# Use double quotes inside single quotes
sentence2 = 'He said "Python is great"'
print(sentence2)

# Empty string
empty_str = ""  
empty_str = ''
print("Empty string:", empty_str)


# Multi-line strings - Triple quotes
paragraph = """This is line 1
This is line 2
This is line 3"""
print(paragraph)
print(type(paragraph))

paragraph2 = '''This is also
a multi-line
string'''
print(paragraph2)
print(type(paragraph2))

# length of a string
word = "Hello"
print("Length of word:", len(word))  # 5

# String is a sequence of characters
sample_str = "Hello"

"""
    H -> 0
    e -> 1
    l -> 2  
    l -> 3
    o -> 4
    Indexing starts from 0
"""
# It starts from index 0
# len - 1 is the last index
# Accessing characters using indexing
first_char = sample_str[0]   # 'H'
second_char = sample_str[1]  # 'e'
third_char = sample_str[2]   # 'l'
fourth_char = sample_str[3]   # 'l'
last_char = sample_str[4]    # 'o'
print("First character:", first_char)
print("Second character:", second_char)
print("Third character:", third_char)   
print("Fourth character:", fourth_char)   
print("Last character:", last_char)


# Accessing characters using negative indexing
# It starts from -1
last_char = sample_str[-1]    # 'o'
fourth_char = sample_str[-2]   # 'l'
third_char = sample_str[-3]  # 'l'
second_char = sample_str[-4]   # 'e'
first_char = sample_str[-5]   # 'H'
# error_char =  sample_str[-6] # IndexError 
print("First character:", first_char)
print("Second character:", second_char)
print("Third character:", third_char)  
print("Fourth character:", fourth_char)    
print("Last character:", last_char)
# print("Error character:", error_char)

sample_str = "heElo WORLD"

# 1. Changing case of strings

# Converting to uppercase
upper_str = sample_str.upper()
print("Uppercase:", upper_str)

# Converting to lowercase
lower_str = sample_str.lower()
print("Lowercase:", lower_str)

# Converting into title case
title_str = sample_str.title()
print("Title Case:", title_str)

# String capitalizing
capitalized_str = sample_str.capitalize()
print("Capitalized:", capitalized_str)

# 2. Removing whitespace
whitespace_str = "   Hello World!   "

# Removing leading and trailing whitespace
stripped_str = whitespace_str.strip()
print("Stripped String:", stripped_str)

# Removing leading whitespace
leading_str = whitespace_str.lstrip()
print("Leading Whitespace Removed:", leading_str)

# Removing trailing whitespace
trailing_str = whitespace_str.rstrip()
print("Trailing Whitespace Removed:", trailing_str)


# 3. Finding substrings
main_str = "Hello, welcome to my coding journey, hello Python world."
"""
Finding the first occurrence of a substring
It is case-sensitive
Returns -1 if not found
"""
first_index = main_str.find("hello")  # Case-sensitive
print("First occurrence of 'hello':", first_index)  # -1 if not found

# 4. Replacing substrings
# Replacing all occurrences of a substring
# It needs two arguments: (old substring, new substring)
# It case-sensitive
replaced_str = main_str.replace("hello", "hi")  # Case-sensitive
print("Replaced String:", replaced_str)


# 5. Checking what string contains (returns True / False)
word = "python123"

# Check if all characters are alphabetic
is_alpha = word.isalpha()
print("Is alphabetic:", is_alpha)  # False
word2 = "Python"
print("Is alphabetic:", word2.isalpha())  # True
print("Pratik".isalpha())  # True

# Check if all characters are numeric
is_numeric = word.isdigit() 
print("Is numeric:", is_numeric)  # False
word3 = "12345"
print("Is numeric:", word3.isdigit())  # True
print("67890".isdigit())  # True

# Check if all characters are alphanumeric (letters+numbers, no special characters, no spaces,  only letters, only numbers)
# returns True if all characters are either letters or numbers
# returns False if there are any special characters
# returns False if the string is empty  - for all built-in functions
is_alnum = word.isalnum()
print("Is alphanumeric:", is_alnum)  # True
word4 = "Python3"
print("Is alphanumeric:", word4.isalnum())  # True
print("Python@3".isalnum())  # False

# returns true if only letters or only numbers
print("HelloWorld".isalnum())  # True
print("12345".isalnum())  # True


# Check if all characters are lowercase
word5 = "python"
is_lower = word5.islower()
print("Is lowercase:", is_lower)  # True
word6 = "Python"
print("Is lowercase:", word6.islower())  # False


# Check if all characters are uppercase
word7 = "PYTHON"        
is_upper = word7.isupper()
print("Is uppercase:", is_upper)  # True
word8 = "Python"
print("Is uppercase:", word8.isupper())  # False


# Check if string contains only whitespace characters
whitespace_str = "   "
is_space = whitespace_str.isspace()
print("Is whitespace only:", is_space)  # True
whitespace_str2 = "   \t\n"             # Tabs and newlines are also whitespace
is_space = whitespace_str2.isspace()
print("Is whitespace only:", is_space)  # True
whitespace_str3 = "  Hello  "
print("Is whitespace only:", whitespace_str3.isspace())  # False

"""
special examples ->
isupper()-->
    "HELLO123"	True	All alphabets uppercase
    "HeLLO123"	False	Lowercase exists
    "12345"	    False	No alphabets
    "HELLO!!"	True	Symbols ignored
    
    ** same works for islower()
"""

# 6. Splitting and joining strings

# When we slipt a string, it becomes a list of substrings
# When there is no parameter given to split(), it splits by whitespace by default
sample_str = "Hello World! Welcome to Python programming."
# Splitting the string into a list of words
words_list = sample_str.split()  # Split by space
print("List of words:", words_list)

fruits_str = "apple,banana,cherry,date"
# Splitting the string into a list of fruits using comma as separator
fruits_list = fruits_str.split(",")  # Split by comma
print("List of fruits:", fruits_list)



# Joining the list of words back into a single string
# When we join it become a single string again
# We can specify the joiner while joining
# It doesnt have any default separator in the beginning
joined_str = " ".join(words_list)  # Join with space
print("Joined string:", joined_str)

joined_str_comma = "-".join(fruits_list)  # Join with comma
print("Joined string with commas:", joined_str_comma)



# 7. startswith() and endswith() methods
# It checks if the string starts or ends with the specified substring
# It returns True or False
# This is case-sensitive
test_str = "Hello, welcome to Python programming."
# Check if the string starts with "Hello"
starts_with_hello = test_str.startswith("Hello") # hello will return False
print("Starts with 'Hello':", starts_with_hello)
starts_with_helloji = test_str.startswith("Helloji")
print("Starts with 'Helloji':", starts_with_helloji)

# Check if the string ends with "programming."
ends_with_programming = test_str.endswith("programming.")
print("Ends with 'programming.':", ends_with_programming)
ends_with_java = test_str.endswith("java")
print("Ends with 'java':", ends_with_java)


# 8.count() method
# It counts the number of occurrences of a substring in the string
# This is case-sensitive
count_str = "Python is great. Python is dynamic. Python is easy to learn."
# Count occurrences of "Python"
python_count = count_str.count("Python")  # 3
print("Occurrences of 'Python':", python_count)
# Count occurrences of "is"
is_count = count_str.count("is")  # 3
print("Occurrences of 'is':", is_count)
# Count occurrences of "java"
java_count = count_str.count("java")  # 0
print("Occurrences of 'java':", java_count)
# Count occurrences of "s"
s_count = count_str.count("s")  # 4
print("Occurrences of 's':", s_count)


# VVVIMP
# Slicing strings
# Slicing allows us to extract a portion of a string using indexing
# last index is not included   vvvimp point
# default start is 0 and default end is length of string
# syntax: string_name[start:end]   
slice_str = "pythonprogramming"
# Extracting substring from index 0 to 5 (not including 5)
substring1 = slice_str[0:5]  # 'pytho'
print("Substring from index 0 to 5:", substring1)
substring_default_start = slice_str[:6]  # 'python'
print("Substring from start to index 6:", substring_default_start)
substring_default_end = slice_str[6:]  # 'programming'
print("Substring from index 6 to end:", substring_default_end)
substring_default_start_and_end = slice_str[:]  # 'pythonprogramming'
print("Substring with default start and end:", substring_default_start_and_end)

# Extracting substring using negative indexing
substring2 = slice_str[-4:-1]  # 'min'
print("Substring from index -4 to -1:", substring2)


# Concatenation
# Concatenation is the process of joining two or more strings into a single string
# It is done using the + operator
str1 = "Hello"
str2 = "World"
concatenated_str = str1 + " " + str2
print("Concatenated string:", concatenated_str)


# Repetition
# Repetition is the process of creating a new string by repeating an existing string multiple times
# It is done using the * operator
repeated_str = str1 * 3
print("Repeated string:", repeated_str)


# String with numbers
age = 25
# This will give error:
# message = "Age is " + age  # Error -> TypeError: Can't add string and int
# print(message)

# Solution 1: Convert number to string
message = "Age is " + str(age) 
print(message)

# Solution 2: Use comma in print
print("Age is", age)

# Solution 3: f-strings (modern way - we'll learn in detail later)
message = f"Age is {age} {32} {45} {str(age)}"
print(message)


name = "Peter"
mobile_number = "1234337890"
# Example: Using f-strings to create an email template
email_body = f"""
Hi,{name}
we are conducting a survey for you.
Kindly confirm your mobile number: {mobile_number}
"""
print(email_body)
