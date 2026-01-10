#==================================================================================
# PRINT STATEMENT EXAMPLES
#==================================================================================
# print using double quotes and single quotes
print("This is our first program in Python using double quotes")
print('This is our first program in Python using single quotes')

# print strings with quotes inside
print("He said, 'Python is awesome!'")
print('She replied, "Indeed, it is!"')

# print numbers (no need for quotes) - labeled output
print("Number 1:", 42)
print("Number 2:", 23)

# print multiple items
print("The answer is", 42)   # comma => default separator is space
print("Sum of", 20, "and", 22, "is", 42)
print("Words:", "Pratik", "loves", "Python")
print("Multiple numbers:", 23, 45, 67, 89)

# print with custom separator
print("Pratik","Loves","Coding", sep="-")
print("Pratik","Loves","Coding", sep='-')
print("Arrow sep:", 22, 23, 24, sep=" > ")

# Printing without newline (using end)
print("Hello", end=" ")
print("World")  # Both print on same line

# Empty print (creates blank line)
print()
print("------------------------------------")

# Print using special characters
print("My name is Pratik\nI love coding")  # \n creates new line
print("Hello\tAasim")  # \t creates tab space

# Formatted printing examples
name = "Pratik"
age = 25
height = 5.8

# Using str.format()
print("Using format(): {} is {} years old and {:.1f}ft tall".format(name, age, height))

# Using f-strings (Python 3.6+)
print(f"Using f-string: {name} is {age} years old and {height:.1f}ft tall")

# Using formatted separator and end
print("A", "B", "C", sep="|", end=" <-- end\n")


