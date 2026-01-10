#==================================================================================
# COMPLEX (complex) DATA TYPE IN PYTHON
#==================================================================================
"""
Notes:
- complex numbers have a real and imaginary part (a + bj)
- Python uses 'j' for the imaginary unit (e.g., 3 + 4j)
- Mixing int/float with complex yields complex results
"""

z1 = 2 + 3j
z2 = -1 - 4j
z3 = 5.0 + 0j
z4 = 0 + 2j
print("Complex numbers:", z1, z2, z3, z4)
print("Type of z1:", type(z1))

# Real and imaginary parts
print("z1.real:", z1.real)
print("z1.imag:", z1.imag)

# Basic operations
a = 2 + 3j
b = 1 - 4j
print("a + b:", a + b)
print("a - b:", a - b)
print("a * b:", a * b)
print("a / b:", a / b)

# Conjugate and magnitude
z = 3 + 4j
print("conjugate:", z.conjugate())
print("abs(z):", abs(z))  # magnitude

# Creating complex via complex()
c1 = complex(2, 3)
c2 = complex(5, -1)
c3 = complex(7)
c4 = complex("2+3j")
print(c1, c2, c3, c4)

# Mixing with int/float
x = 5
y = 2.5
print("x + z:", x + z)
print("y + z:", y + z)

# Useful example: impedance
r = 4
x_react = 3
impedance = complex(r, x_react)
print("Impedance:", impedance)

# End of complex examples
