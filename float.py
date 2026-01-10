#==================================================================================
# FLOAT (float) DATA TYPE IN PYTHON
#==================================================================================
"""
Notes:
- float represents decimal numbers (e.g., 3.14, -0.5)
- Division always produces float (unless using //)
- Use round() to control decimal places
"""

x = 3.14
y = -2.5
z = 0.0
print("Floats:", x, y, z)
print("Type of x:", type(x))

# Arithmetic
a = 5.5
b = 2.0
print("a + b:", a + b)
print("a - b:", a - b)
print("a * b:", a * b)
print("a / b:", a / b)
print("a // b:", a // b)
print("a % b:", a % b)
print("a ** b:", a ** b)

# Mixing with int
p = 10
q = 3.5
print("p + q:", p + q)
print("p * q:", p * q)
print("p / q:", p / q)

# Comparisons
m = 10.5
n = 20.0
print("m == n:", m == n)
print("m != n:", m != n)

# Conversions
num_int = 5
num_float = float(num_int)
print("float(5):", num_float)
print("float('2.25'):", float("2.25"))

# Rounding
pi = 3.14159265
print("round(pi):", round(pi))
print("round(pi, 2):", round(pi, 2))

# End of float examples
