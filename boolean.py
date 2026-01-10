#==================================================================================
# BOOLEAN (bool) DATA TYPE IN PYTHON
#==================================================================================
"""
NOTES:
- Boolean has only two values: True and False (capital T and F)
- Comparison and logical operators return boolean values
- Many Python constructs evaluate to Truthy or Falsy values
"""

# Examples of boolean variables
is_active = True
is_logged_in = False

print("is_active:", is_active)
print("is_logged_in:", is_logged_in)

# Check data type
print("Type of is_active:", type(is_active))     # <class 'bool'>
print("Type of is_logged_in:", type(is_logged_in))  # <class 'bool'>


# ----- BOOLEAN FROM COMPARISONS ----- #
# Comparison operators always return boolean

a = 10
b = 20

print("a == b:", a == b)   # False
print("a != b:", a != b)   # True
print("a > b:", a > b)    # False
print("a < b:", a < b)    # True
print("a >= 10:", a >= 10)  # True
print("b <= 20:", b <= 20)  # True


# ----- BOOLEAN FROM LOGICAL OPERATORS ----- #

# AND operator
# True only if BOTH conditions are True
print("True and True ->", True and True)    # True
print("True and False ->", True and False)   # False
print("False and True ->", False and True)   # False
print("False and False ->", False and False)  # False

# OR operator
# True if ANY ONE condition is True
print("True or True ->", True or True)    # True
print("True or False ->", True or False)    # True
print("False or True ->", False or True)    # True
print("False or False ->", False or False)   # False

# NOT operator
# Reverses the value
print("not True ->", not True)   # False
print("not False ->", not False)  # True


# ----- BOOLEAN IN CONDITIONS (if-else) ----- #

age = 18

if age >= 18:
    print("You are eligible to vote")
else:
    print("You are not eligible to vote")


# ----- VALUES THAT MEAN TRUE AND FALSE IN PYTHON ----- #
# (Truthy and Falsy values)
print("bool(True):", bool(True))
print("bool(1):", bool(1))
print("bool(-1):", bool(-1))
print("bool(10):", bool(10))
print("bool('Hello'):", bool("Hello"))
print("bool(' '):", bool(" "))       # space is still a character
print("bool([1, 2]):", bool([1, 2]))
print("bool((0,)):", bool((0,)))
print("bool({1,3,4}):", bool({1,3,4}))
print("bool({'a': 1}):", bool({"a": 1}))

# FALSY VALUES (treated as False)
print("bool(False):", bool(False))
print("bool(0):", bool(0))
print("bool(0.0):", bool(0.0))
print("bool(""):", bool(""))        # empty string
print("bool([]):", bool([]))
print("bool(()):", bool(()))
print("bool({}):", bool({}))
print("bool(set()):", bool(set()))
print("bool(None):", bool(None))


# ----- BOOLEAN FROM bool() FUNCTION ----- #
# bool() converts values into True or False
b1 = bool(100)
print("bool(100):", b1)          # True

b2 = bool("")
print("bool(""):", b2)          # False

b3 = bool("Python")
print("bool('Python'):", b3)          # True

b4 = bool([])
print("bool([]):", b4)          # False

b5 = bool([0])
print("bool([0]):", b5)          # True



# ----- BOOLEAN RETURNING STRING METHODS ----- #
# These methods return True or False

text = "Python"

print("text.isalpha():", text.isalpha())  # True
print("text.isdigit():", text.isdigit())  # False
print("text.isupper():", text.isupper())  # False
print("text.islower():", text.islower())  # False


# ----- REAL-LIFE BOOLEAN EXAMPLES ----- #

is_raining = True
has_umbrella = False

if not is_raining and has_umbrella:
    print("You can go outside")
else:
    print("Better stay inside")


logged_in = True

if logged_in:
    print("Show dashboard")
else:
    print("Show login page")


# homework
# admin = 101
# hr = 102
# employee1 = 201
# employee2 = 202

# id = ????

# comparison operators with string
# name = latik
# 2. if name == "Pratik":
#       print("Welcome Admin")
# 3. else:
#       print("Welcome User")
