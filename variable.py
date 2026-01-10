#==================================================================================
# VARIABLES & NAMING CONVENTIONS
#==================================================================================
"""
Short notes on variable naming and best practices:
- Use descriptive snake_case names (e.g., student_age)
- Start with a letter or underscore; do not start with a digit
- Avoid spaces and special characters; do not use Python keywords
- Variables are case-sensitive (name, Name, NAME are different)
"""
# Storing string in Variable
name = "Pratik"
print("name:", name)


# Storing number in Variable
num = 25
print("num:", num)


# Case sensitivity
name = "John"
Name = "Jane"
NAME = "Jack"

# All three are DIFFERENT variables (different memory location)
print("id(name):", id(name), "value:", name)   # John
print("id(Name):", id(Name), "value:", Name)   # Jane
print("id(NAME):", id(NAME), "value:", NAME)   # Jack


# Assign same value to diff variables
# a = 2
# b = 2
# c = 2
a = b = c = 2 
print("a:", a)
print("b:", b)
print("c:", c)


# Assign multiple values to multiple variables
a, b , c = 1, 2 , 3      # if we have 3 variables we must have 3 values else it will give error - > value error
print("a:", a)
print("b:", b)
print("c:", c)


# Assign different data type values to multiple variables
name, age, email = "Pratik", 25, "abc@gmail.com"
print("name:", name)
print("age:", age)
print("email:", email)


# Swapping
a = "Pratik"
b = "Aasim"
print("Before swap - a:", a)
print("Before swap - b:", b)

print("After swapping (method 1):")
# Method 1.
temp = a
a = b
b = temp
print("temp:", temp)
print("a:", a)
print("b:", b)

# Method 2.
a, b = b, a   # Pythonic way of swapping
print("After swapping (method 2) - a:", a)
print("After swapping (method 2) - b:", b)




















