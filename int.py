#==================================================================================
# INTEGER (int) DATA TYPE IN PYTHON
#==================================================================================
"""
Notes:
- int represents whole numbers (e.g., 10, -5, 0)
- Common operations: +, -, *, /, //, %, **
- Converting float->int truncates the decimal part (not rounding)
- Converting strings with non-integer content raises ValueError
"""

# Basic integers and types
a = 10
b = -20
c = 0
print("Integers:", a, b, c)
print("Type of a:", type(a))

# Arithmetic examples
x = 10
y = 3
print("x + y:", x + y)
print("x - y:", x - y)
print("x * y:", x * y)
print("x / y:", x / y)    # normal division -> float
print("x // y:", x // y)  # floor division -> int
print("x % y:", x % y)    # remainder
print("x ** y:", x ** y)  # exponent

# Comparison examples
print("x == y:", x == y)
print("x != y:", x != y)
print("x > y:", x > y)
print("x < y:", x < y)

# Type conversion
f1 = 3.9
print("int(3.9) ->", int(f1))  # 3 (decimal removed)

s = "42"
print("int('42') ->", int(s))
# int("10.5")  # ValueError: invalid literal for int() with base 10: '10.5'

# End of int examples
