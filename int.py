#==================================================================================
# INT (INTEGER) DATA TYPE IN PYTHON
#==================================================================================

# int means: whole number without decimal point

a = 10
b = -20
c = 0

print("Integers:", a, b, c)

# To check the data type 
print("Type of a:", type(a))   # <class 'int'>
print("Type of b:", type(b))   # <class 'int'>
print("Type of c:", type(c))   # <class 'int'>


# ----- BASIC ARITHMETIC OPERATIONS WITH int ----- #

a = 10
b = 3

# Addition
print("a + b:", a + b)   # 13

# Subtraction
print("a - b:", a - b)   # 7

# Multiplication
print("a * b:", a * b)   # 30

# Division – / vs //
print("a / b:", a / b)   # 3.3333333333 (normal division, result is float)
print("a // b:", a // b)  # 3            (floor division, result is int)

# / → normal division (can give decimal)
# // → "cut off" the decimal part (floor division)


# Remainder (Modulo)
print("a % b:", a % b)   # 1

# % gives remainder after division.
# Example: 10 / 3 is 3 with remainder 1 → % gives 1.


# Power (Exponent)
print("a ** b:", a ** b)  # 10 ** 3 = 1000

# a ** b means "a to the power b".


# ----- COMPARISON OPERATORS WITH int ----- #

# Comparison always returns True or False (returns boolean val).

x = 10
y = 20

print("x == y:", x == y)   # False
print("x != y:", x != y)   # True
print("x > y:", x > y)    # False
print("x < y:", x < y)    # True
print("x >= 10:", x >= 10)  # True
print("y <= 20:", y <= 20)  # True


# ----- TYPE CONVERSION (CASTING) WITH int ----- #

# float -> int (cuts off decimal part)
f1 = 3.9
f2 = 5.1

print(int(f1))   # 3  (not 4, decimal part is removed)
print(int(f2))   # 5

# string -> int (string must be a whole number)
s1 = "10"
s2 = "20"

print("int('10'):", int(s1))   # 10
print("int('20'):", int(s2))   # 20

# Invalid conversions (will give error if you try)
# int("10.5")    # ValueError (string has decimal)
# int("abc")     # ValueError
