#==================================================================================
# FLOAT DATA TYPE IN PYTHON
#==================================================================================

# Float means: number with decimal point

x = 3.14
y = -2.5
z = 0.0

print("Floats:", x, y, z)

# To check the data type
print("Type of x:", type(x))   # <class 'float'>
print("Type of y:", type(y))   # <class 'float'>
print("Type of z:", type(z))   # <class 'float'>


# Basic arithmetic operations with float

a = 5.5
b = 2.0

# Addition
print("a + b:", a + b)   # 7.5

# Subtraction
print("a - b:", a - b)   # 3.5

# Multiplication
print("a * b:", a * b)   # 11.0

# Division
print("a / b:", a / b)   # 2.75 (normal division, result is float)

# Floor division //
print("a // b:", a // b)  # 2.0 (cuts off decimal part, result is still float)

# Remainder (Modulo)
print("a % b:", a % b)   # 1.5

# Power (Exponent)
print("a ** b:", a ** b)  # 5.5 ** 2.0 = 30.25


# Mixing int and float

p = 10      # int
q = 3.5     # float

print("p + q:", p + q)   # 13.5 (float)
print("p * q:", p * q)   # 35.0 (float)
print("p / q:", p / q)   # 2.857142857142857 (float)


# Comparison operators with float

m = 10.5
n = 20.0

print("m == n:", m == n)    # False
print("m != n:", m != n)    # True
print("m > n:", m > n)     # False
print("m < n:", m < n)     # True
print("m >= 10.5:", m >= 10.5) # True
print("n <= 20.0:", n <= 20.0) # True


# Type conversion (casting) with float

# int -> float
num_int = 5
num_float = float(num_int)
print("num_int:", num_int, "->", type(num_int))       # 5 <class 'int'>
print("num_float:", num_float, "->", type(num_float))   # 5.0 <class 'float'>

# string -> float
s1 = "3.5"
s2 = "10"
print("float('3.5'):", float(s1))    # 3.5
print("float('10'):", float(s2))    # 10.0

# Invalid conversions (will give error if you try)
# float("abc")     # ValueError
# float("10a")     # ValueError


# ----- BUILT-IN FUNCTIONS AND USEFUL THINGS WITH FLOAT ----- #

# type() - to check the data type
val = 4.75
print("Type of val:", type(val))    # <class 'float'>

# float() - to convert other types to float
print("float(7):", float(7))         # 7.0 (int -> float)
print("float('2.25'):", float("2.25"))    # 2.25 (string -> float)

# round() - to round float values

pi = 3.14159265

print(round(pi))       # 3      (rounded to nearest integer) -> if >= 0.50= next integer(ex.3.6=4)
print(round(pi, 2))    # 3.14   (2 decimal places)
print(round(pi, 3))    # 3.141  (3 decimal places)

# End of float examples
