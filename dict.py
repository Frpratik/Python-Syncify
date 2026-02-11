#==================================================================================
# DICTIONARY (dict) DATA TYPE IN PYTHON
#==================================================================================
"""
NOTES:
- Dictionary is an unordered collection of key-value pairs
- Dictionary is mutable (changeable)
- Dictionary keys must be unique (no duplicate keys)
- Dictionary keys must be immutable (string, number, tuple)
- Dictionary values can be any data type and can be duplicated
- Dictionary is written using curly braces {} with key:value pairs
- Very fast lookup by key - O(1) time complexity
"""

# Creating dictionaries
student = {"name": "Alice", "age": 20, "grade": "A"}
numbers_dict = {1: "one", 2: "two", 3: "three"}
mixed_dict = {"name": "John", "age": 25, "scores": [85, 90, 78], "active": True,(1,2,3):"tuplevalue"}

print("Student dictionary:", student)
print("Numbers dictionary:", numbers_dict)
print("Mixed dictionary:", mixed_dict)

# Check data type
print("Type of student:", type(student))

#==================================================================================
# EMPTY DICTIONARY
#==================================================================================
"""
NOTES:
- Empty dictionary is created using {} or dict()
- Used when key-value pairs will be added later dynamically
"""

empty_dict = {}
print("\nEmpty dictionary using {}:", empty_dict)
print("Type:", type(empty_dict))

empty_dict2 = dict()
print("Empty dictionary using dict():", empty_dict2)
print("Type:", type(empty_dict2))

#==================================================================================
# CREATING DICTIONARIES (DIFFERENT METHODS)
#==================================================================================
"""
NOTES:
- Multiple ways to create dictionaries
- dict() constructor can take keyword arguments
- dict() can convert list of tuples to dictionary
"""

# Using dict() constructor with keyword arguments
person = dict(name="Bob", age=30, city="New York")
print("\nDictionary using dict():", person)

# Using dict() with list of tuples
pairs = [("a", 1), ("b", 2), ("c", 3)]
dict_from_pairs = dict(pairs)
print("Dictionary from list of tuples:", dict_from_pairs)

#==================================================================================
# DICTIONARY KEYS MUST BE IMMUTABLE
#==================================================================================
"""
NOTES:
- Valid keys: string, number, tuple (with immutable elements)
- Invalid keys: list, dict, set (mutable types)
"""

# Valid keys
valid_dict = {
    "name": "Alice",           # string key
    42: "answer",              # integer key
    3.14: "pi",                # float key
    (1, 2): "tuple key",       # tuple key
    True: "boolean key"        # boolean key
}
print("\nDictionary with various key types:", valid_dict)

# Invalid keys (will cause errors)
# invalid_dict = {[1, 2]: "value"}  # TypeError: unhashable type: 'list'
# invalid_dict = {{1, 2}: "value"}  # TypeError: unhashable type: 'set'
# invalid_dict = {{"a": 1}: "value"}  # TypeError: unhashable type: 'dict'
print("Lists, sets, and dicts cannot be dictionary keys")

#==================================================================================
# ACCESSING DICTIONARY VALUES
#==================================================================================
"""
NOTES:
- Access values using keys in square brackets []
- Raises KeyError if key doesn't exist
- get() method is safer - returns None or default value if key missing
"""

student = {"name": "Alice", "age": 20, "grade": "A", "city": "Boston"}
print("\nStudent dictionary:", student)

# Using square brackets
print("Name:", student["name"])
print("Age:", student["age"])

# KeyError if key doesn't exist
# print(student["phone"])  # KeyError: 'phone'
print("Accessing non-existent key raises KeyError")

# Using get() method (safer)
print("\nUsing get() method:")
print("Name:", student.get("name"))
print("Phone (doesn't exist):", student.get("phone"))
print("Phone with default:", student.get("phone", "Not available"))

#==================================================================================
# ADDING AND MODIFYING DICTIONARY ITEMS
#==================================================================================
"""
NOTES:
- Add new key-value pair: dict[key] = value
- Modify existing value: dict[key] = new_value
- If key exists, value is updated; if not, new pair is added
- update() - to add multiple key:value pairs
"""

person = {"name": "John", "age": 25}
print("\nOriginal dictionary:", person)

# Adding new key-value pair
person["city"] = "New York"
print("After adding city:", person)

person["email"] = "john@example.com"
print("After adding email:", person)

# Modifying existing value
person["age"] = 26
print("After modifying age:", person)

person["name"] = "John Doe"
print("After modifying name:", person)

# Adding multiple items using update()
person.update({"phone": "123-456-7890", "country": "USA"})
print("After update():", person)

#==================================================================================
# LENGTH OF DICTIONARY
#==================================================================================
"""
NOTES:
- len() returns number of key-value pairs
"""

my_dict = {"a": 1, "b": 2, "c": 3, "d": 4}
print("\nDictionary:", my_dict)
print("Length (number of key-value pairs):", len(my_dict))

empty = {}
print("Length of empty dictionary:", len(empty))

#==================================================================================
# CHECKING IF KEY EXISTS IN DICTIONARY
#==================================================================================
"""
NOTES:
- 'in' operator checks if key exists
- 'not in' operator checks if key doesn't exist
- Very fast operation - O(1) time complexity
- Only checks keys, not values
"""

student = {"name": "Alice", "age": 20, "grade": "A"}
print("\nStudent dictionary:", student)

print("Is 'name' in dictionary?", "name" in student)
print("Is 'phone' in dictionary?", "phone" in student)
print("Is 'phone' not in dictionary?", "phone" not in student)

# Checking before accessing
if "email" in student:
    print("Email:", student["email"])
else:
    print("Email not found in dictionary")

#==================================================================================
# REMOVING ITEMS FROM DICTIONARY
#==================================================================================
"""
NOTES:
- pop(key) - removes and returns value, raises KeyError if not found
- pop(key, default) - removes and returns value, returns default if not found
- popitem() - removes and returns last inserted key-value pair (Python 3.7+)
- del dict[key] - deletes key-value pair
- clear() - removes all items
"""

# Using pop()
person = {"name": "Alice", "age": 20, "city": "Boston", "grade": "A"}
print("\nOriginal dictionary:", person)

removed_age = person.pop("age")
print("Popped age:", removed_age)
print("After pop('age'):", person)

# pop() with default value
phone = person.pop("phone", "No phone")
print("Popped phone (with default):", phone)
print("Dictionary unchanged:", person)

# pop() without default raises KeyError
# person.pop("email")  # KeyError: 'email'
print("pop() without default raises KeyError if key not found")

# Using popitem() - removes last inserted item
last_item = person.popitem()
print("\nPopped last item:", last_item)
print("After popitem():", person)

# Using del
del person["city"]
print("After del person['city']:", person)

# del with non-existent key raises KeyError
# del person["phone"]  # KeyError: 'phone'

# Using clear()
temp_dict = {"a": 1, "b": 2, "c": 3}
temp_dict.clear()
print("\nAfter clear():", temp_dict)

# Deleting entire dictionary
del_dict = {"x": 1, "y": 2}
del del_dict
# print(del_dict)  # NameError: name 'del_dict' is not defined
print("Dictionary deleted using del")

#==================================================================================
# DICTIONARY METHODS
#==================================================================================
"""
NOTES:
- keys() - returns all keys
- values() - returns all values
- items() - returns all key-value pairs as tuples
- get() - safely access value
- update() - merge dictionaries
# - setdefault() - get value or set default if key doesn't exist
- copy() - create shallow copy
"""

sample = {"name": "Alice", "age": 20, "grade": "A", "city": "Boston"}
print("\nSample dictionary:", sample)

# keys() method
print("\nAll keys:", sample.keys())
print("Keys as list:", list(sample.keys()))

# values() method
print("\nAll values:", sample.values())
print("Values as list:", list(sample.values()))

# items() method
print("\nAll items:", sample.items())
print("Items as list:", list(sample.items()))

# get() method
print("\nget('name'):", sample.get("name"))
print("get('phone', 'N/A'):", sample.get("phone", "N/A"))

# update() method - merge dictionaries
sample.update({"phone": "123-456", "email": "alice@example.com"})
print("\nAfter update():", sample)

# update() can also modify existing keys
sample.update({"age": 21})
print("After updating age:", sample)

# setdefault() method
# print("\nUsing setdefault():")
# country = sample.setdefault("country", "USA")
# print("Country:", country)
# print("Dictionary after setdefault():", sample)

# # setdefault() doesn't change existing keys
# name = sample.setdefault("name", "Bob")
# print("Name (unchanged):", name)

#==================================================================================
# ITERATING THROUGH DICTIONARY
#==================================================================================
"""
NOTES:
- Can iterate through keys, values, or items
- Default iteration is over keys
- Use items() for both keys and values
"""

student = {"name": "Alice", "age": 20, "grade": "A", "city": "Boston"}

# Iterating over keys (default)
print("\nIterating over keys:")
for key in student:
    print(key)

# Explicitly using keys()
print("\nUsing keys():")
for key in student.keys():
    print(key)

# Iterating over values
print("\nIterating over values:")
for value in student.values():
    print(value)

# Iterating over items (key-value pairs)
print("\nIterating over items:")
for key, value in student.items():
    print(f"{key}: {value}")

# Using enumerate with items
# print("\nUsing enumerate with items:")
# for index, (key, value) in enumerate(student.items(), 1):
#     print(f"{index}. {key}: {value}")

#==================================================================================
# DICTIONARY COMPREHENSION
#==================================================================================
"""
NOTES:
- Similar to list comprehension but creates dictionary
- Syntax: {key_expr: value_expr for item in iterable}
- Can include conditions
- Very powerful for transforming data
"""

# Basic dictionary comprehension
squares = {x: x**2 for x in range(1, 6)}
# squares = [x**2 for x in range(1, 6)]   => [2,4,6,8,10]   #list comprehension
print("\nSquares dictionary:", squares)

# Dictionary comprehension with condition
even_squares = {x: x**2 for x in range(1, 11) if x % 2 == 0}
print("Even squares:", even_squares)

# Converting list of tuples to dictionary
pairs = [("a", 1), ("b", 2), ("c", 3)]
dict_comp = {k: v for k, v in pairs}
print("From list of tuples:", dict_comp)

# Swapping keys and values
original = {"a": 1, "b": 2, "c": 3}
swapped = {v: k for k, v in original.items()}
print("\nOriginal:", original)
print("Swapped:", swapped)

# Dictionary comprehension with string
# char_count = {char: word.count(char) for char in "hello"}
word = "hello"
char_positions = {char: word.count(char) for char in set(word)}
print("\nCharacter count in 'hello':", char_positions)

# Filtering dictionary
prices = {"apple": 0.5, "banana": 0.3, "orange": 0.8, "grape": 1.2}
expensive = {k: v for k, v in prices.items() if v > 0.5}
print("\nAll prices:", prices)
print("Expensive items (> 0.5):", expensive)

#==================================================================================
# NESTED DICTIONARIES
#==================================================================================
"""
NOTES:
- Dictionaries can contain other dictionaries
- Useful for representing complex hierarchical data
- Access using multiple keys
"""

# user_data = {
#     "personal_details": {
#         "name": "Alice",
#         "age": 25,
#         "city": "New York"
#     },
#     "education_details": {
#         "degree": "Bachelor of Science",
#         "major": "Computer Science",
#         "university": "University of XYZ"
#     },
#     "employment_details": {
#         "company": "ABC Company",
#         "position": "Software Engineer",
#         "salary": 60000
#     }
# }
# for i in user_data["education_details"]:
#     print(i)

# Simple nested dictionary
students = {
    "student1": {"name": "Alice", "age": 20, "grade": "A"},
    "student2": {"name": "Bob", "age": 22, "grade": "B"},
    "student3": {"name": "Charlie", "age": 21, "grade": "A"}
}

print("\nNested dictionary:")
print(students)

# Accessing nested values
print("\nStudent1 name:", students["student1"]["name"])
print("Student2 grade:", students["student2"]["grade"])

# Iterating through nested dictionary
print("\nAll students:")
for student_id, info in students.items():
    print(f"{student_id}:")
    for key, value in info.items():
        print(f"  {key}: {value}")

# Modifying nested dictionary
students["student1"]["age"] = 21
print("\nAfter modifying student1 age:", students["student1"])

# Adding to nested dictionary
students["student4"] = {"name": "David", "age": 23, "grade": "B"}
print("After adding student4:", students.keys())

# Deeply nested dictionary
company = {
    "HR": {
        "employees": {
            "emp1": {"name": "Alice", "position": "Manager"},
            "emp2": {"name": "Bob", "position": "Recruiter"}
        }
    },
    "IT": {
        "employees": {
            "emp3": {"name": "Charlie", "position": "Developer"},
            "emp4": {"name": "David", "position": "Admin"}
        }
    }
}

print("\nDeeply nested - IT Developer name:")
print(company["IT"]["employees"]["emp3"]["name"])

#==================================================================================
# COPYING DICTIONARIES
#==================================================================================
"""
NOTES:
- Assignment (=) creates reference, not copy
- copy() creates shallow copy
- dict() constructor creates shallow copy
- Shallow copy: nested objects are still referenced
- Use copy.deepcopy() for complete independent copy
"""

# Reference (not a copy)
original = {"a": 1, "b": 2, "c": 3}
reference = original
reference["d"] = 4
print("\nOriginal after modifying reference:", original)
print("Reference:", reference)
print("Both point to same dictionary")

# Shallow copy using copy()
original2 = {"a": 1, "b": 2, "c": 3}
copied = original2.copy()
copied["d"] = 4
print("\nOriginal2:", original2)
print("Copied:", copied)
print("Modifications don't affect original")

# Shallow copy using dict()
original3 = {"x": 10, "y": 20}
copied2 = dict(original3)
copied2["z"] = 30
print("\nOriginal3:", original3)
print("Copied2:", copied2)

# Shallow copy limitation with nested dictionaries
nested_original = {"a": 1, "b": {"c": 2}}
nested_copy = nested_original.copy()
nested_copy["b"]["c"] = 999
print("\nNested original (affected!):", nested_original)
print("Nested copy:", nested_copy)
print("Shallow copy shares nested objects")

# Deep copy for nested dictionaries
import copy
nested_original2 = {"a": 1, "b": {"c": 2}}
deep_copied = copy.deepcopy(nested_original2)
deep_copied["b"]["c"] = 999
print("\nNested original2 (not affected):", nested_original2)
print("Deep copied:", deep_copied)
print("Deep copy creates independent nested objects")

#==================================================================================
# MERGING DICTIONARIES
#==================================================================================
"""
NOTES:
- update() merges dictionaries (modifies original)
- {**dict1, **dict2} unpacking (Python 3.5+)
- dict1 | dict2 union operator (Python 3.9+)
"""

dict1 = {"a": 1, "b": 2}
dict2 = {"c": 3, "d": 4}

# Using update()
dict1_copy = dict1.copy()
dict1_copy.update(dict2)
print("\nMerged using update():", dict1_copy)

# Using unpacking
merged = {**dict1, **dict2}
print("Merged using unpacking:", merged)

# Using | operator (Python 3.9+)
merged2 = dict1 | dict2
print("Merged using | operator:", merged2)

# Overlapping keys (later overwrites earlier)
dict_a = {"a": 1, "b": 2, "c": 3}
dict_b = {"b": 20, "d": 4}
merged3 = {**dict_a, **dict_b}
print("\ndict_a:", dict_a)
print("dict_b:", dict_b)
print("Merged (b overwritten):", merged3)

# Merging multiple dictionaries
dict_x = {"x": 1}
dict_y = {"y": 2}
dict_z = {"z": 3}
all_merged = {**dict_x, **dict_y, **dict_z}
print("\nMerging three dictionaries:", all_merged)

# #==================================================================================
# # DICTIONARY WITH DEFAULT VALUES (defaultdict)
# #==================================================================================
# """
# NOTES:
# - defaultdict from collections module
# - Provides default value for non-existent keys
# - Avoids KeyError
# - Useful for counting, grouping, etc.
# """

# from collections import defaultdict

# # defaultdict with int (default 0)
# counts = defaultdict(int)
# print("\ndefaultdict with int:")
# print("counts['a'] before assignment:", counts["a"])
# counts["a"] += 1
# counts["b"] += 1
# counts["a"] += 1
# print("After counting:", dict(counts))

# # defaultdict with list (default empty list)
# groups = defaultdict(list)
# print("\ndefaultdict with list:")
# groups["fruits"].append("apple")
# groups["fruits"].append("banana")
# groups["vegetables"].append("carrot")
# print("Groups:", dict(groups))

# # defaultdict with lambda for custom default
# scores = defaultdict(lambda: "Not Available")
# print("\ndefaultdict with lambda:")
# scores["Alice"] = 95
# print("Alice's score:", scores["Alice"])
# print("Bob's score (default):", scores["Bob"])
# print("Scores:", dict(scores))

# #==================================================================================
# # ORDERED DICTIONARY (OrderedDict)
# #==================================================================================
# """
# NOTES:
# - OrderedDict from collections module
# - Maintains insertion order (regular dict does this in Python 3.7+)
# - OrderedDict has move_to_end() method
# - Equality considers order for OrderedDict
# """

# from collections import OrderedDict

# # Regular dict maintains order (Python 3.7+)
# regular = {"a": 1, "b": 2, "c": 3}
# print("\nRegular dict:", regular)

# # OrderedDict
# ordered = OrderedDict()
# ordered["a"] = 1
# ordered["b"] = 2
# ordered["c"] = 3
# print("OrderedDict:", ordered)

# # move_to_end() method
# ordered.move_to_end("a")
# print("After move_to_end('a'):", ordered)

# ordered.move_to_end("c", last=False)
# print("After move_to_end('c', last=False):", ordered)

# # Equality comparison
# dict1 = {"a": 1, "b": 2}
# dict2 = {"b": 2, "a": 1}
# print("\nRegular dicts equal (order doesn't matter):", dict1 == dict2)

# od1 = OrderedDict([("a", 1), ("b", 2)])
# od2 = OrderedDict([("b", 2), ("a", 1)])
# print("OrderedDicts equal (order matters):", od1 == od2)

#==================================================================================
# DICTIONARY SORTING
#==================================================================================
"""
NOTES:
- sorted() returns sorted list of keys
- Can sort by keys or values
- Use items() with key parameter for custom sorting
"""

scores = {"Alice": 85, "Bob": 92, "Charlie": 78, "David": 95}
print("\nOriginal scores:", scores)

# Sort by keys
sorted_keys = sorted(scores)
print("Sorted keys:", sorted_keys)
# sorted_dict_by_keys = {k: scores[k] for k in sorted_keys}
# print("Dict sorted by keys:", sorted_dict_by_keys)

# # Sort by values
# sorted_by_values = dict(sorted(scores.items(), key=lambda item: item[1]))
# print("Dict sorted by values:", sorted_by_values)

# # Sort by values (descending)
# sorted_desc = dict(sorted(scores.items(), key=lambda item: item[1], reverse=True))
# print("Dict sorted by values (descending):", sorted_desc)

# # Using sorted() with dictionary comprehension
# sorted_dict = {k: v for k, v in sorted(scores.items(), key=lambda item: item[1], reverse=True)}
# print("Using comprehension:", sorted_dict)

#==================================================================================
# BUILT-IN FUNCTIONS WITH DICTIONARIES
#==================================================================================
"""
NOTES:
- len() - number of key-value pairs
- max() - maximum key
- min() - minimum key
- sum() - sum of keys (if numeric)
- any() - True if any key is True
- all() - True if all keys are True
"""
sample_dict = {"a": 10, "b": 20, "c": 30}
print("\nSample dictionary:", sample_dict)
print("Length:", len(sample_dict))
print("Max key:", max(sample_dict))
print("Min key:", min(sample_dict))

# # Max/Min by value
# print("Max by value:", max(sample_dict, key=sample_dict.get))
# print("Min by value:", min(sample_dict, key=sample_dict.get))
# print("Max value:", max(sample_dict.values()))
# print("Min value:", min(sample_dict.values()))

# # Sum of values
# print("Sum of values:", sum(sample_dict.values()))

# # any() and all()
# dict1 = {1: "a", 2: "b", 3: "c"}
# dict2 = {0: "a", 1: "b", 2: "c"}
# print("\ndict1 keys:", dict1.keys())
# print("all() on keys:", all(dict1.keys()))
# print("\ndict2 keys:", dict2.keys())
# print("all() on keys (has 0):", all(dict2.keys()))
# print("any() on keys:", any(dict2.keys()))

#==================================================================================
# CONVERTING BETWEEN DATA TYPES
#==================================================================================
"""
NOTES:
- Can convert list of tuples to dictionary
- Can convert dictionary to list of tuples
- Can create dictionary from two lists using zip
"""

# List of tuples to dictionary
pairs = [("name", "Alice"), ("age", 20), ("grade", "A")]
dict_from_list = dict(pairs)
print("\nList of tuples:", pairs)
print("Converted to dict:", dict_from_list)

# Dictionary to list of tuples
sample = {"a": 1, "b": 2, "c": 3}
list_of_tuples = list(sample.items())
print("\nDictionary:", sample)
print("Converted to list of tuples:", list_of_tuples)

# # Two lists to dictionary using zip
# names = ["Alice", "Bob", "Charlie"]
# ages = [20, 22, 21]
# people = dict(zip(names, ages))
# print("\nNames:", names)
# print("Ages:", ages)
# print("Dictionary from zip:", people)

# Dictionary keys to list
keys_list = list(sample.keys())
print("\nDictionary keys as list:", keys_list)

# Dictionary values to list
values_list = list(sample.values())
print("Dictionary values as list:", values_list)

#==================================================================================
# REAL-LIFE DICTIONARY EXAMPLES
#==================================================================================
"""
NOTES:
- Dictionaries are perfect for key-value data relationships
- Common in real-world applications
"""

# Example 1: Student Records
print("\n--- EXAMPLE 1: STUDENT RECORDS ---")
students_db = {
    "S001": {"name": "Alice", "age": 20, "grade": "A", "major": "CS"},
    "S002": {"name": "Bob", "age": 22, "grade": "B", "major": "Math"},
    "S003": {"name": "Charlie", "age": 21, "grade": "A", "major": "CS"}
}

print("Student S001:", students_db["S001"])
print("\nAll students:")
for student_id, info in students_db.items():
    print(f"{student_id}: {info['name']}, Grade: {info['grade']}")

# Example 2: Word Counter
print("\n--- EXAMPLE 2: WORD FREQUENCY COUNTER ---")
text = "hello world hello python python python world"
words = text.split()
word_count = {}

for word in words:
    word_count[word] = word_count.get(word, 0) + 1

print("Text:", text)
print("Word frequency:", word_count)

# Using defaultdict for counting
from collections import defaultdict
word_count2 = defaultdict(int)
for word in words:
    word_count2[word] += 1
print("Using defaultdict:", dict(word_count2))

# Example 3: Phone Book
print("\n--- EXAMPLE 3: PHONE BOOK ---")
phonebook = {
    "Alice": "123-456-7890",
    "Bob": "234-567-8901",
    "Charlie": "345-678-9012"
}

print("Phonebook:", phonebook)
print("Alice's number:", phonebook.get("Alice", "Not found"))
print("David's number:", phonebook.get("David", "Not found"))

# Add new contact
phonebook["David"] = "456-789-0123"
print("After adding David:", phonebook)

# Example 4: Shopping Cart
print("\n--- EXAMPLE 4: SHOPPING CART ---")
cart = {
    "apple": {"price": 0.5, "quantity": 5},
    "banana": {"price": 0.3, "quantity": 10},
    "orange": {"price": 0.8, "quantity": 3}
}

print("Shopping cart:")
total = 0
for item, details in cart.items():
    item_total = details["price"] * details["quantity"]
    total += item_total
    print(f"{item.capitalize()}: ${details['price']} × {details['quantity']} = ${item_total:.2f}")

print(f"\nTotal cost: ${total:.2f}")

# Example 5: Configuration Settings
print("\n--- EXAMPLE 5: APPLICATION CONFIG ---")
config = {
    "debug": True,
    "database": {
        "host": "localhost",
        "port": 5432,
        "name": "mydb",
        "user": "admin"
    },
    "api_keys": {
        "weather": "abc123",
        "maps": "xyz789"
    },
    "max_connections": 100
}

print("Debug mode:", config["debug"])
print("Database host:", config["database"]["host"])
print("Weather API key:", config["api_keys"]["weather"])

# Example 6: Grade Book
print("\n--- EXAMPLE 6: GRADE BOOK ---")
gradebook = {
    "Alice": [85, 90, 88, 92],
    "Bob": [78, 82, 80, 85],
    "Charlie": [92, 95, 90, 93]
}

print("Grade book:")
for student, grades in gradebook.items():
    average = sum(grades) / len(grades)
    print(f"{student}: Grades: {grades}, Average: {average:.2f}")

# Example 7: Inventory Management
print("\n--- EXAMPLE 7: INVENTORY MANAGEMENT ---")
inventory = {
    "P001": {"name": "Laptop", "quantity": 15, "price": 999.99},
    "P002": {"name": "Mouse", "quantity": 50, "price": 24.99},
    "P003": {"name": "Keyboard", "quantity": 30, "price": 79.99}
}

print("Inventory:")
total_value = 0
for product_id, details in inventory.items():
    value = details["quantity"] * details["price"]
    total_value += value
    print(f"{product_id}: {details['name']}, Stock: {details['quantity']}, Value: ${value:.2f}")

print(f"\nTotal inventory value: ${total_value:.2f}")

# Update inventory
inventory["P001"]["quantity"] -= 2
print("\nAfter selling 2 laptops:")
print(f"Laptops in stock: {inventory['P001']['quantity']}")

# Example 8: User Authentication
print("\n--- EXAMPLE 8: USER AUTHENTICATION ---")
users = {
    "alice": {"password": "pass123", "role": "admin", "email": "alice@example.com"},
    "bob": {"password": "secret456", "role": "user", "email": "bob@example.com"}
}

def authenticate(username, password):
    if username in users and users[username]["password"] == password:
        return True, users[username]["role"]
    return False, None

# Test authentication
username = "alice"
password = "pass123"
is_valid, role = authenticate(username, password)
if is_valid:
    print(f"Login successful! Role: {role}")
else:
    print("Invalid credentials")

