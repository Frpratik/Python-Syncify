#==================================================================================
# STRING (str) DATA TYPE IN PYTHON
#==================================================================================
"""
Notes:
- Strings are sequences of characters
- Use single/double/triple quotes for different needs
- Many built-in methods help inspect and transform strings
"""

# Creating strings
name = "John Doe"
message = 'Hello World'
print("name:", name)
print("message:", message)

# Quotes inside strings
sentence1 = "Python's syntax is easy"
sentence2 = 'He said "Python is great"'
print(sentence1)
print(sentence2)

# Empty and multi-line strings
empty_str = ""
print("Empty string:", repr(empty_str))
paragraph = """Line1
Line2
Line3"""
print(paragraph)

# Indexing and slicing
sample_str = "Hello"
print("First char:", sample_str[0])
print("Last char:", sample_str[-1])
print("Slice [0:3]:", sample_str[0:3])

# Useful methods
s = "  Hello World  "
print("strip():", s.strip())
print("upper():", s.upper())
print("lower():", s.lower())

# Find and replace
main_str = "hello, welcome to my coding journey, hello Python world."
print("find('hello'):", main_str.find("hello"))
print("replace ->", main_str.replace("hello", "hi"))

# Split and join
words_list = "Hello World! Welcome".split()
print("split():", words_list)
print("join():", "-".join(words_list))

# startswith / endswith / isalpha / isdigit
print("startswith('Hello'):", "Hello World".startswith("Hello"))
print("isdigit('123'):", "123".isdigit())

# Formatted strings
age = 25
print(f"Using f-string: Age is {age}")

# End of string examples
