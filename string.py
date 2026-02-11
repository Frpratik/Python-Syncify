#==================================================================================
# STRING (str) - Text data
#==================================================================================

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
# error_char =  sample_str[5] # IndexError -> IndexError: string index out of range
print("First character:", first_char)
print("Second character:", second_char)
print("Third character:", third_char)   
print("Fourth character:", fourth_char)   
print("Last character:", last_char)
# print("Error character:", error_char)


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
main_str = "hello, welcome to my coding journey, hello Python world."
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
joined_str = "".join(words_list)  # Join with space
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
print("join():", "-".join(words_list))

# startswith / endswith / isalpha / isdigit
print("startswith('Hello'):", "Hello World".startswith("Hello"))
print("isdigit('123'):", "123".isdigit())

# Formatted strings
age = 25
print(f"Using f-string: Age is {age}")

# End of string examples
