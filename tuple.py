#==================================================================================
# TUPLE (tuple) DATA TYPE IN PYTHON
#==================================================================================
"""
NOTES:
- Tuple is an ordered collection of elements
- Tuple is IMMUTABLE (cannot be changed after creation) -> imp -> but if tuple contains mutable objects (like lists), those can be modified
- Tuple allows duplicate values
- Tuple can store multiple data types
- Tuples are faster than lists
- Tuples use less memory than lists
- Tuples can be used as dictionary keys (lists cannot)
"""

# Creating tuples
numbers_tuple = (1, 2, 3, 4, 5)
names_tuple = ("Alice", "Bob", "Charlie")
mixed_tuple = (1, "Python", 3.14, True, [1, 2], {"name": "John"})

print("Numbers tuple:", numbers_tuple)
print("Names tuple:", names_tuple)
print("Mixed tuple:", mixed_tuple)

# Check data type
print("Type of numbers_tuple:", type(numbers_tuple))

# Tuple with duplicates (allowed)
duplicate_tuple = (1, 2, 2, 3, 3, 3, 4)
print("Tuple with duplicates:", duplicate_tuple)

#==================================================================================
# SINGLE ELEMENT TUPLE (IMPORTANT!)
#==================================================================================
"""
NOTES:
- Single element tuple MUST have trailing comma
- Without comma, it's just a value in parentheses, not a tuple
- This is a common mistake for beginners
"""

# Correct single element tuple
single_tuple = (5,)
print("\nSingle element tuple:", single_tuple)
print("Type:", type(single_tuple))

# Wrong - this is NOT a tuple
not_a_tuple = (5)
print("Not a tuple (just integer):", not_a_tuple)
print("Type:", type(not_a_tuple))

# Single element with trailing comma
single_string_tuple = ("hello",)
print("Single string tuple:", single_string_tuple)
print("Type:", type(single_string_tuple))

#==================================================================================
# TUPLE WITHOUT PARENTHESES (TUPLE PACKING)
#==================================================================================
"""
NOTES:
- Tuples can be created without parentheses
- Comma makes it a tuple, not parentheses
- Parentheses are optional but recommended for clarity
"""

# Tuple without parentheses
packed_tuple = 1, 2, 3, 4
print("\nTuple created without parentheses:", packed_tuple)
print("Type:", type(packed_tuple))

# Single element without parentheses
single_packed = 5,
print("Single element tuple without parentheses:", single_packed)
print("Type:", type(single_packed))

#==================================================================================
# EMPTY TUPLE
#==================================================================================
"""
NOTES:
- Empty tuple is created with empty parentheses ()
- Less common than empty lists since tuples are immutable
"""

empty_tuple = ()
print("\nEmpty tuple:", empty_tuple)
print("Type:", type(empty_tuple))
print("Length of empty tuple:", len(empty_tuple))

empty_tuple = tuple()
print("Empty tuple using tuple() constructor:", empty_tuple)
print("Type:", type(empty_tuple))
print("Length of empty tuple:", len(empty_tuple))

#==================================================================================
# TUPLE INDEXING
#==================================================================================
"""
NOTES:
- Tuple is a sequence type like lists
- Indexing starts from 0
- Positive index: access from start
- Negative index: access from end
"""

sample_tuple = ("a", "b", "c", "d", "e")
print("\nSample tuple:", sample_tuple)
print("First element [0]:", sample_tuple[0])
print("Second element [1]:", sample_tuple[1])
print("Last element [4]:", sample_tuple[4])

# Negative indexing
print("Last element [-1]:", sample_tuple[-1])
print("Second last element [-2]:", sample_tuple[-2])
print("First element using negative index [-5]:", sample_tuple[-5])

# Index out of range error
# print(sample_tuple[10])  # IndexError: tuple index out of range

#==================================================================================
# LENGTH OF TUPLE
#==================================================================================
"""
NOTES:
- len() returns number of elements in the tuple
- Counts all elements including duplicates
"""

my_tuple = (10, 20, 30, 40, 50)
print("\nTuple:", my_tuple)
print("Length of tuple:", len(my_tuple))

duplicate_tuple = (1, 1, 2, 2, 3, 3)
print("Tuple with duplicates:", duplicate_tuple)
print("Length (counts duplicates):", len(duplicate_tuple))

#==================================================================================
# TUPLE SLICING
#==================================================================================
"""
NOTES:
- Slicing extracts part of the tuple
- Returns a new tuple
- Last index is NOT included
- Syntax: tuple[start:end:step]
- Original tuple remains unchanged
"""

print("\nSample tuple for slicing:", sample_tuple)
print("Elements [0:3]:", sample_tuple[0:3])
print("Elements [:3]:", sample_tuple[:3])
print("Elements [2:]:", sample_tuple[2:])
print("All elements [:]:", sample_tuple[:])
print("Elements [-3:-1]:", sample_tuple[-3:-1])
print("Every second element [::2]:", sample_tuple[::2])
print("Elements with step 2 [1:5:2]:", sample_tuple[1:5:2])

# Reverse tuple using slicing
print("Reversed tuple [::-1]:", sample_tuple[::-1])
print("Reverse with step 2 [::-2]:", sample_tuple[::-2])

#==================================================================================
# TUPLE IS IMMUTABLE (VERY IMPORTANT!)
#==================================================================================
"""
NOTES:
- Cannot modify, add, or remove elements after creation
- Cannot change element values
- This is the KEY difference between tuples and lists
- Immutability makes tuples faster and more memory efficient
- Immutability allows tuples to be used as dictionary keys
"""

immutable_tuple = (10, 20, 30)
print("\nOriginal tuple:", immutable_tuple)

# Cannot modify elements
# immutable_tuple[0] = 100  # TypeError: 'tuple' object does not support item assignment
print("Cannot modify tuple elements - tuples are immutable")

#==================================================================================
# TUPLE WITH MUTABLE ELEMENTS (IMPORTANT CONCEPT!)
#==================================================================================
"""
NOTES:
- Tuple itself is immutable
- But if tuple contains mutable objects (like lists), those can be modified
- This is an important distinction in Python
"""

tuple_with_list = (1, 2, [3, 4, 5])
print("\nTuple with list inside:", tuple_with_list)

# Cannot change tuple itself
# tuple_with_list[0] = 100  # TypeError

# But can modify the mutable object inside
tuple_with_list[2].append(6)
print("After modifying list inside tuple:", tuple_with_list)

tuple_with_list[2][0] = 999
print("After changing list element:", tuple_with_list)

print("Tuple structure unchanged, but list content modified")

#==================================================================================
# TUPLE CONCATENATION
#==================================================================================
"""
NOTES:
- Can combine tuples using + operator
- Creates a NEW tuple
- Original tuples remain unchanged
- Cannot use += on tuple variable (creates new tuple)
"""

tuple1 = (1, 2, 3)
tuple2 = (4, 5, 6)
print("\ntuple1:", tuple1)
print("tuple2:", tuple2)
print("Concatenated tuple1 + tuple2:", tuple1 + tuple2)
print("Original tuple1:", tuple1)
print("Original tuple2:", tuple2)

# In list, if we create same variable for concatenation it will be changed due to mutability
# but with tupple it will create new address and will be at that address
# l1 = [1,2,3]
# l2 = [4,5,6]
# l1 = l1 + l2
# print("Concatenated l1 + l2:", l1)
# print("Original l1:", l1)
# print("Original l2:", l2)


# Multiple concatenation
tuple3 = (7, 8)
combined = tuple1 + tuple2 + tuple3
print("Combining three tuples:", combined)

# Using += (creates new tuple)
tuple_x = (1, 2)
print("\nOriginal tuple_x:", tuple_x)
print("ID of tuple_x:", id(tuple_x))
tuple_x += (3, 4)
print("After tuple_x += (3, 4):", tuple_x)
print("ID of new tuple_x (different):", id(tuple_x))
print("Note: += creates a new tuple, doesn't modify original")

#==================================================================================
# TUPLE REPETITION
#==================================================================================
"""
NOTES:
- Can repeat tuples using * operator
- Creates a new tuple with repeated elements
- Useful for initialization
"""

repeat_tuple = (1, 2, 3)
print("\nOriginal tuple:", repeat_tuple)
print("Repeated 3 times:", repeat_tuple * 3)
print("Repeated 2 times:", repeat_tuple * 2)

# Creating tuple with same value
zeros = (0,) * 5
print("Tuple of 5 zeros:", zeros)

# Empty tuple repetition
empty = () * 10
print("Empty tuple repeated:", empty)

#==================================================================================
# CHECKING ELEMENT IN TUPLE (MEMBERSHIP OPERATORS)
#==================================================================================
"""
NOTES:
- 'in' operator checks if element exists
- 'not in' operator checks if element doesn't exist
- Returns True or False
- Searches through entire tuple (slower for large tuples)
"""

fruits_tuple = ("apple", "banana", "cherry", "date")
print("\nFruits tuple:", fruits_tuple)
print("Is 'banana' in tuple?", "banana" in fruits_tuple)
print("Is 'grape' in tuple?", "grape" in fruits_tuple)
print("Is 'grape' not in tuple?", "grape" not in fruits_tuple)

numbers = (10, 20, 30, 40, 50)
print("\nNumbers tuple:", numbers)
print("Is 30 in tuple?", 30 in numbers)
print("Is 100 in tuple?", 100 in numbers)

#==================================================================================
# TUPLE METHODS (ONLY 2 METHODS!)
#==================================================================================
"""
NOTES:
- Tuples have only 2 methods (because they're immutable)
- count(value) - returns number of occurrences
- index(value) - returns first index of value
- No methods for modification (append, remove, etc.)
"""

# count() method
sample = (1, 2, 2, 3, 2, 4, 5, 2)
print("\nSample tuple:", sample)
print("Count of 2:", sample.count(2))
print("Count of 1:", sample.count(1))
print("Count of 10 (not in tuple):", sample.count(10))

letters = ("a", "b", "c", "a", "a", "d")
print("\nLetters tuple:", letters)
print("Count of 'a':", letters.count("a"))
print("Count of 'z':", letters.count("z"))

# index() method
fruits = ("apple", "banana", "cherry", "banana", "date")
print("\nFruits tuple:", fruits)
print("Index of 'cherry':", fruits.index("cherry"))
print("Index of 'banana' (first occurrence):", fruits.index("banana"))

# index() with start and end parameters
print("Index of 'banana' starting from index 2:", fruits.index("banana", 2))
print("Index of 'banana' between index 2 and 5:", fruits.index("banana", 2, 5))

# ValueError if element not found
# print(fruits.index("grape"))  # ValueError: tuple.index(x): x not in tuple
print("index() raises ValueError if element not found")

#==================================================================================
# TUPLE UNPACKING (VERY IMPORTANT!)
#==================================================================================
"""
NOTES:
- Tuple unpacking assigns tuple elements to variables
- Number of variables must match number of elements 
- Very useful for returning multiple values from functions
- Makes code more readable and Pythonic
"""

# Basic unpacking
coordinates = (10, 20)
x, y = coordinates
print("\nTuple:", coordinates)
print("x:", x)
print("y:", y)

# Unpacking with multiple values
person = ("John", 25, "Engineer")
name, age, profession = person
print("\nPerson tuple:", person)
print("Name:", name)
print("Age:", age)
print("Profession:", profession)


#==================================================================================
# NESTED TUPLES
#==================================================================================
"""
NOTES:
- Tuples can contain other tuples
- Useful for representing complex data structures
- Access using multiple indices
"""

# 2D tuple (like a matrix)
matrix = (
    (1, 2, 3),
    (4, 5, 6),
    (7, 8, 9)
)
print("\nMatrix tuple:")
print(matrix)
print("First row:", matrix[0])
print("Element at [1][2]:", matrix[1][2])
print("Last element:", matrix[2][2])

# Tuple of tuples
students = (
    ("Alice", 85, "A"),
    ("Bob", 92, "A+"),
    ("Charlie", 78, "B")
)

print("\nAccessing nested data:")
print("First student name:", students[0][0])
print("Second student grade:", students[1][2])

# Deeply nested tuple
nested = (1, (2, (3, (4, 5))))
print("\nDeeply nested tuple:", nested)
print("Access innermost 5:", nested[1][1][1][1])


#==================================================================================
# TUPLE COMPARISON
#==================================================================================
"""
NOTES:
- Tuples can be compared using comparison operators
- First different element determines the result
- If all elements equal and same length, tuples are equal
"""

tuple_a = (1, 2, 3)
tuple_b = (1, 2, 3)
tuple_c = (1, 2, 4)
tuple_d = (5, 2)

print("\ntuple_a:", tuple_a)
print("tuple_b:", tuple_b)
print("tuple_c:", tuple_c)
print("tuple_d:", tuple_d)

print("\nComparisons:")
print("tuple_a == tuple_b:", tuple_a == tuple_b)
print("tuple_a == tuple_c:", tuple_a == tuple_c)
print("tuple_a < tuple_c:", tuple_a < tuple_c)
print("tuple_a > tuple_c:", tuple_a > tuple_c)
print("tuple_a > tuple_d:", tuple_a > tuple_d)

# String tuple comparison
words1 = ("apple", "banana")
words2 = ("apple", "cherry")
print("\nwords1:", words1)
print("words2:", words2)
print("words1 < words2:", words1 < words2)

#==================================================================================
# CONVERTING BETWEEN DATA TYPES
#==================================================================================
"""
NOTES:
- Can convert list to tuple
- Can convert tuple to list
- Can convert string to tuple
- Can convert set to tuple
- Can convert range to tuple
"""

# List to Tuple
my_list = [1, 2, 3, 4, 5]
tuple_from_list = tuple(my_list)
print("\nList:", my_list)
print("Converted to tuple:", tuple_from_list)

# Tuple to List
my_tuple = (10, 20, 30)
list_from_tuple = list(my_tuple)
print("\nTuple:", my_tuple)
print("Converted to list:", list_from_tuple)

# String to Tuple
text = "hello"
tuple_from_string = tuple(text)
print("\nString:", text)
print("Converted to tuple:", tuple_from_string)

# Set to Tuple
my_set = {3, 1, 4, 2}
tuple_from_set = tuple(my_set)
print("\nSet:", my_set)
print("Converted to tuple:", tuple_from_set)

# Range to Tuple
range_obj = range(1, 6)
tuple_from_range = tuple(range_obj)
print("\nRange object:", range_obj)
print("Converted to tuple:", tuple_from_range)

# Dictionary to Tuple (keys only)
# my_dict = {"a": 1, "b": 2, "c": 3}
# tuple_from_dict = tuple(my_dict)
# print("\nDictionary:", my_dict)
# print("Tuple of keys:", tuple_from_dict)

# # Dictionary items to tuple
# tuple_from_items = tuple(my_dict.items())
# print("Tuple of key-value pairs:", tuple_from_items)

#==================================================================================
# TUPLE AS DICTIONARY KEY (IMPORTANT USE CASE!)
#==================================================================================
"""
NOTES:
- Tuples can be used as dictionary keys (lists cannot)
- Must contain only immutable elements
- Useful for composite keys
- Common in real-world applications
"""

# Using tuple as dictionary key
locations = {
    (40.7128, -74.0060): "New York",
    (51.5074, -0.1278): "London",
    (35.6762, 139.6503): "Tokyo"
}
print("\nDictionary with tuple keys:")
print(locations)
print("Location at (51.5074, -0.1278):", locations[(51.5074, -0.1278)])

# Multi-dimensional dictionary
grades = {
    ("Alice", "Math"): 95,
    ("Alice", "Science"): 88,
    ("Bob", "Math"): 82,
    ("Bob", "Science"): 90
}
print("\nStudent grades:")
print("Alice's Math grade:", grades[("Alice", "Math")])
print("Bob's Science grade:", grades[("Bob", "Science")])

# Cannot use list as key
# invalid_dict = {[1, 2]: "value"}  # TypeError: unhashable type: 'list'
print("\nLists cannot be dictionary keys (mutable)")
print("Tuples can be dictionary keys (immutable)")
 
#==================================================================================
# TUPLE COMPREHENSION (DOESN'T EXIST - RETURNS GENERATOR!) -> Advance concept 
#==================================================================================
# """
# NOTES:
# - (x for x in ...) creates generator, not tuple
# - Use tuple() constructor to convert generator to tuple
# - Generator is memory efficient for large datasets
# """

# # This creates a generator, not tuple
# gen = (x**2 for x in range(5))
# print("\nGenerator expression:", gen)
# print("Type:", type(gen))

# # Convert generator to tuple
# squares_tuple = tuple(x**2 for x in range(5))
# print("Tuple from generator:", squares_tuple)
# print("Type:", type(squares_tuple))

# # Comparing memory
# import sys
# large_tuple = tuple(range(10000))
# large_gen = (x for x in range(10000))
# print("\nTuple size in bytes:", sys.getsizeof(large_tuple))
# print("Generator size in bytes:", sys.getsizeof(large_gen))
# print("Generator is much more memory efficient!")

#==================================================================================
# BUILT-IN FUNCTIONS WITH TUPLES
#==================================================================================
"""
NOTES:
- len() - number of elements
- max() - maximum element (must be comparable)
- min() - minimum element (must be comparable)
- sum() - sum of numeric elements
- sorted() - returns sorted list
- any() - True if any element is True
- all() - True if all elements are True
"""

numbers_tuple = (45, 12, 78, 23, 56)
print("\nNumbers tuple:", numbers_tuple)
print("Length:", len(numbers_tuple))
print("Maximum:", max(numbers_tuple))
print("Minimum:", min(numbers_tuple))
print("Sum:", sum(numbers_tuple))
print("Sorted (returns list):", sorted(numbers_tuple))
print("Sorted descending:", sorted(numbers_tuple, reverse=True))

# any() and all()
bool_tuple1 = (True, True, True)
bool_tuple2 = (True, False, True)
bool_tuple3 = (False, False, False)

print("\nbool_tuple1:", bool_tuple1)
print("all():", all(bool_tuple1))
print("any():", any(bool_tuple1))

print("\nbool_tuple2:", bool_tuple2)
print("all():", all(bool_tuple2))
print("any():", any(bool_tuple2))

print("\nbool_tuple3:", bool_tuple3)
print("all():", all(bool_tuple3))
print("any():", any(bool_tuple3))

# Using any() and all() with conditions
numbers = (2, 4, 6, 8, 10)
print("\nNumbers:", numbers)
print("All even?", all(x % 2 == 0 for x in numbers))
print("Any greater than 5?", any(x > 5 for x in numbers))

#==================================================================================
# ADVANTAGES OF TUPLES OVER LISTS -> for extra knowledge
#==================================================================================
"""
NOTES:
ADVANTAGES:
1. Faster than lists (iteration, access)
2. Use less memory than lists
3. Immutable - data protection
4. Can be used as dictionary keys  -> it is hashable
5. Can be used in sets
6. Safer for data that shouldn't change

WHEN TO USE TUPLES:
- Data should not change
- Need to use as dictionary key
- Returning multiple values from function
- Performance is critical
"""

print("\n--- TUPLE VS LIST COMPARISON ---")

# Memory comparison
import sys
list_data = [1, 2, 3, 4, 5]
tuple_data = (1, 2, 3, 4, 5)

print("List size:", sys.getsizeof(list_data), "bytes")
print("Tuple size:", sys.getsizeof(tuple_data), "bytes")
print("Tuple uses less memory!")

# Tuples in sets (lists cannot be in sets)
set_of_tuples = {(1, 2), (3, 4), (5, 6)}
print("\nSet of tuples:", set_of_tuples)
# set_of_lists = {[1, 2], [3, 4]}  # TypeError: unhashable type: 'list'
print("Lists cannot be added to sets (mutable)")

#==================================================================================
# REAL-LIFE TUPLE EXAMPLES
#==================================================================================
"""
NOTES:
- Tuples are perfect for immutable, related data
- Common in real-world scenarios
"""

# Example 1: RGB Color Values
print("\n--- EXAMPLE 1: RGB COLORS ---")
red = (255, 0, 0)
green = (0, 255, 0)
blue = (0, 0, 255)
white = (255, 255, 255)
black = (0, 0, 0)

print("Red color:", red)
print("Green color:", green)
print("Accessing red channel:", red[0])

def display_color(color_tuple):
    r, g, b = color_tuple
    print(f"RGB({r}, {g}, {b})")

display_color(blue)

# Example 2: Geographic Coordinates
print("\n--- EXAMPLE 2: COORDINATES ---")
new_york = (40.7128, -74.0060)
london = (51.5074, -0.1278)
tokyo = (35.6762, 139.6503)

cities = {
    new_york: "New York",
    london: "London",
    tokyo: "Tokyo"
}

print("Cities and coordinates:")
for coords, name in cities.items():
    lat, lon = coords
    print(f"{name}: Latitude {lat}, Longitude {lon}")

# Example 3: Date and Time
print("\n--- EXAMPLE 3: DATE REPRESENTATION ---")
date1 = (2025, 12, 23)  # year, month, day
date2 = (2025, 1, 1)

print("Date 1:", date1)
year, month, day = date1
print(f"Formatted: {day}/{month}/{year}")

def format_date(date_tuple):
    y, m, d = date_tuple
    return f"{d:02d}/{m:02d}/{y}"

print("Formatted date:", format_date(date2))

# Example 4: Database Records
print("\n--- EXAMPLE 4: DATABASE RECORDS ---")
employees = [
    (1, "Alice", "Engineering", 75000),
    (2, "Bob", "Marketing", 65000),
    (3, "Charlie", "Sales", 70000),
    (4, "David", "Engineering", 80000)
]

print("Employee Database:")
for emp in employees:
    emp_id, name, dept, salary = emp
    print(f"ID: {emp_id}, Name: {name}, Dept: {dept}, Salary: ${salary}")

# Filter engineers
engineers = [emp for emp in employees if emp[2] == "Engineering"]
print("\nEngineers only:")
for emp in engineers:
    print(emp)

# Example 5: Configuration Settings
print("\n--- EXAMPLE 5: IMMUTABLE CONFIGURATION ---")
# Configuration that should not change
DATABASE_CONFIG = (
    "localhost",    # host
    5432,           # port
    "mydb",         # database name
    "admin"         # username
)

host, port, db_name, user = DATABASE_CONFIG
print(f"Database Config:")
print(f"Host: {host}, Port: {port}, DB: {db_name}, User: {user}")

# Cannot accidentally modify config
# DATABASE_CONFIG[0] = "newhost"  # TypeError
print("Configuration is protected from accidental changes")

#==================================================================================
# END