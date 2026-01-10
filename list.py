#==================================================================================
# LIST (list) DATA TYPE IN PYTHON
#==================================================================================
"""
NOTES:
- List is an ordered collection of elements
- List is mutable (changeable)
- List allows duplicate values
- List can store multiple data types
- List is written using square brackets []
"""

# Creating lists
numbers = [1, 2, 3, 4, 5]
names = ["Alice", "Bob", "Charlie"]
mixed_list = [1, "Python", 3.14, True, [1, 2, 3]]

print("Numbers list:", numbers)
print("Names list:", names)
print("Mixed list:", mixed_list)

# Check data type
print("Type of numbers:", type(numbers))

#==================================================================================
# EMPTY LIST
#==================================================================================
"""
NOTES:
- Empty list means list with no elements
- Used when data will be added later dynamically
"""

empty_list = []
print("\nEmpty list using []:", empty_list)
print("Type of empty list:", type(empty_list))

# Using list() constructor
empty_list2 = list()
print("Empty list using list():", empty_list2)

#==================================================================================
# LIST INDEXING
#==================================================================================
"""
NOTES:
- List is a sequence type
- Indexing starts from 0
- Use positive index from start
- Use negative index from end
"""

sample_list = ["a", "b", "c", "d", "e"]
print("\nSample list:", sample_list)
print("First element [0]:", sample_list[0])
print("Second element [1]:", sample_list[1])
print("Last element [4]:", sample_list[4])

# Negative indexing
print("\nNegative indexing:")
print("Last element [-1]:", sample_list[-1])
print("Second last element [-2]:", sample_list[-2])
print("First element using negative [-5]:", sample_list[-5])

# Index out of range error
# print(sample_list[10])  # IndexError: list index out of range
print("Accessing index out of range raises IndexError")

#==================================================================================
# LENGTH OF LIST
#==================================================================================
"""
NOTES:
- len() returns number of elements in the list
"""

my_list = [10, 20, 30, 40]
print("\nList:", my_list)
print("Length of list:", len(my_list))

empty = []
print("Length of empty list:", len(empty))

#==================================================================================
# LIST SLICING
#==================================================================================
"""
NOTES:
- Slicing extracts part of the list
- Last index is NOT included
- Syntax: list[start:end:step]
"""

sample_list = ["a", "b", "c", "d", "e"]
print("\nSample list for slicing:", sample_list)

print("Elements [0:3]:", sample_list[0:3])
print("Elements [:3]:", sample_list[:3])
print("Elements [2:]:", sample_list[2:])
print("All elements [:]:", sample_list[:])
print("Elements [-3:-1]:", sample_list[-3:-1])

# With step
print("\nSlicing with step:")
print("Every second element [::2]:", sample_list[::2])
print("Elements [1:5:2]:", sample_list[1:5:2])
print("Elements [0:5:3]:", sample_list[0:5:3])

# Reverse using slicing
print("\nReversing list:")
print("Reversed [::-1]:", sample_list[::-1])
print("Reverse with step 2 [::-2]:", sample_list[::-2])

#==================================================================================
# LIST IS MUTABLE (VERY IMPORTANT)
#==================================================================================
"""
NOTES:
- Lists can be modified after creation
- Can change element values
- Can add or remove elements
"""

nums = [10, 20, 30]
print("\nOriginal list:", nums)

nums[0] = 100
print("After changing nums[0] to 100:", nums)

nums[1] = 400
print("After changing nums[1] to 400:", nums)

nums[2] = 500
print("After changing nums[2] to 500:", nums)

#==================================================================================
# ADDING ELEMENTS TO LIST
#==================================================================================
"""
NOTES:
- append() adds element at the end
- insert(index, value) adds element at specific position
- extend() adds elements of another list
"""

# Using append()
nums = [10, 20, 30]
print("\nOriginal list:", nums)

nums.append(40)
print("After append(40):", nums)

nums.append(50)
print("After append(50):", nums)

# Using insert()
nums.insert(2, 25)
print("After insert(2, 25):", nums)

nums.insert(0, 5)
print("After insert(0, 5):", nums)

# If index is out of range, adds at end
nums.insert(100, 60)
print("After insert(100, 60):", nums)

# Using extend()
a = [1, 2, 3]
b = [4, 5, 6]
print("\nList a:", a)
print("List b:", b)

a.extend(b)
print("After a.extend(b):", a)
print("Original list b:", b)

# extend() vs append()
list1 = [1, 2, 3]
list1.append([4, 5])
print("\nUsing append([4, 5]):", list1)

list2 = [1, 2, 3]
list2.extend([4, 5])
print("Using extend([4, 5]):", list2)

#==================================================================================
# REMOVING ELEMENTS FROM LIST
#==================================================================================
"""
NOTES:
- remove(value) - removes first occurrence of value
- pop() - removes and returns last element
- pop(index) - removes and returns element at index
- del - deletes element or slice
- clear() - removes all elements
"""

# Using remove()
nums = [10, 20, 30, 20, 40]
print("\nOriginal list:", nums)

nums.remove(20)
print("After remove(20):", nums)
print("Note: Only first occurrence removed")

# remove() raises ValueError if element not found
# nums.remove(100)  # ValueError: list.remove(x): x not in list
print("remove() raises ValueError if element not found")

# Using pop()
nums = [10, 20, 30, 40, 50]
print("\nOriginal list:", nums)

last_item = nums.pop()
print("Popped last element:", last_item)
print("List after pop():", nums)

# pop() with index
removed_item = nums.pop(1)
print("Popped element at index 1:", removed_item)
print("List after pop(1):", nums)

# pop() on empty list raises IndexError
# empty_list = []
# empty_list.pop()  # IndexError: pop from empty list

# pop() with out of range index
# nums.pop(100)  # IndexError: pop index out of range
print("pop() raises IndexError if index out of range")

# Using del
nums = [10, 20, 30, 40, 50]
print("\nOriginal list:", nums)

del nums[1]
print("After del nums[1]:", nums)

del nums[1:3]
print("After del nums[1:3]:", nums)

# Delete entire list
del_list = [1, 2, 3]
del del_list
# print(del_list)  # NameError: name 'del_list' is not defined
print("List deleted using del")

# Using clear()
temp_list = [1, 2, 3, 4, 5]
print("\nOriginal list:", temp_list)

temp_list.clear()
print("After clear():", temp_list)

#==================================================================================
# CHECKING ELEMENT IN LIST (MEMBERSHIP OPERATORS)
#==================================================================================
"""
NOTES:
- 'in' operator checks if element exists
- 'not in' operator checks if element doesn't exist
- Slower for large lists
"""

my_list = [10, 20, 30, 40, 50]
print("\nList:", my_list)

print("Is 20 in list?", 20 in my_list)
print("Is 100 in list?", 100 in my_list)
print("Is 100 not in list?", 100 not in my_list)

# Checking before accessing
fruits = ["apple", "banana", "cherry"]
if "banana" in fruits:
    print("\nBanana found in list!")
else:
    print("Banana not found")

#==================================================================================
# COUNT & INDEX METHODS
#==================================================================================
"""
NOTES:
- count(value) - returns number of occurrences
- index(value) - returns first index of value
"""

# Using count()
nums = [1, 2, 2, 3, 2, 4, 5, 2]
print("\nList:", nums)
print("Count of 2:", nums.count(2))
print("Count of 1:", nums.count(1))
print("Count of 10 (not in list):", nums.count(10))

letters = ["a", "b", "c", "a", "a", "d"]
print("\nLetters list:", letters)
print("Count of 'a':", letters.count("a"))
print("Count of 'z':", letters.count("z"))

# Using index()
fruits = ["apple", "banana", "cherry", "banana", "date"]
print("\nFruits list:", fruits)
print("Index of 'cherry':", fruits.index("cherry"))
print("Index of 'banana' (first occurrence):", fruits.index("banana"))

# index() raises ValueError if element not found
# print(fruits.index("grape"))  # ValueError: 'grape' is not in list
print("index() raises ValueError if element not found")

#==================================================================================
# SORTING LIST
#==================================================================================
"""
NOTES:
- sort() modifies original list
- sorted() returns new sorted list
- difference between sort() and sorted() => sort() modifies original list and sorted() returns new sorted list
"""

# Using sort()
nums = [5, 2, 9, 1, 3]
print("\nOriginal list:", nums)

nums.sort()
print("After sort():", nums)

nums.sort(reverse=True)
print("After sort(reverse=True):", nums)

# Using sorted()
nums2 = [3, 1, 4, 2]
print("\nOriginal list:", nums2)

sorted_list = sorted(nums2)
print("sorted() returns:", sorted_list)
print("Original list unchanged:", nums2)

sorted_desc = sorted(nums2, reverse=True)
print("sorted(reverse=True) returns:", sorted_desc)

# Sorting strings
names = ["Charlie", "Alice", "Bob"]
print("\nOriginal names:", names)
names.sort()
print("After sort():", names)

#==================================================================================
# REVERSING LIST
#==================================================================================
"""
NOTES:
- reverse() reverses list in place
- Does not sort, just reverses order
"""

nums = [1, 2, 3, 4, 5]
print("\nOriginal list:", nums)

nums.reverse()
print("After reverse():", nums)

# Reversing already reversed list
nums.reverse()
print("After reverse() again:", nums)

#==================================================================================
# COPYING LIST (REFERENCE VS COPY)
#==================================================================================
"""
NOTES:
- Assignment (=) creates reference, not copy
- copy() creates actual copy
- Changes to reference affect original
"""

# Reference (not a copy)
a = [1, 2, 3]
b = a
print("\nOriginal list a:", a)
print("Reference b = a:", b)

b.append(4)
print("\nAfter b.append(4):")
print("List a:", a)
print("List b:", b)
print("Both changed - they point to same list")

# Using copy()
c = [1, 2, 3]
d = c.copy()
print("\nOriginal list c:", c)
print("Copied list d:", d)

d.append(5)
print("\nAfter d.append(5):")
print("List c:", c)
print("List d:", d)
print("Only d changed - independent copy")

# Alternative ways to copy
# original = [1, 2, 3]
# copy1 = original.copy()
# copy2 = original[:]
# copy3 = list(original)

# print("\nAll three methods create independent copies")

#==================================================================================
# LIST CONCATENATION
#==================================================================================
"""
NOTES:
- + operator combines lists
- Creates new list
- Original lists unchanged
"""

list1 = [1, 2, 3]
list2 = [4, 5, 6]
print("\nList1:", list1)
print("List2:", list2)

combined = list1 + list2
print("Combined list:", combined)
print("Original list1:", list1)
print("Original list2:", list2)

# Multiple concatenation
list3 = [7, 8]
result = list1 + list2 + list3
print("\nCombining three lists:", result)

#==================================================================================
# LIST REPETITION
#==================================================================================
"""
NOTES:
- * operator repeats list
- Creates new list with repeated elements
"""

my_list = [1, 2, 3]
print("\nOriginal list:", my_list)
print("Repeated 3 times:", my_list * 3)
print("Repeated 2 times:", my_list * 2)

# Creating list with same value
zeros = [0] * 5
print("\nList of 5 zeros:", zeros)

dashes = ["-"] * 10
print("List of 10 dashes:", dashes)

#==================================================================================
# NESTED LISTS
#==================================================================================
"""
NOTES:
- Lists can contain other lists
- Access using multiple indices
"""

matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

print("\nMatrix (nested list):")
print(matrix)

print("First row:", matrix[0])
print("Second row:", matrix[1])
print("Element at [1][2]:", matrix[1][2])
print("Element at [0][0]:", matrix[0][0])
print("Element at [2][1]:", matrix[2][1])

# Modifying nested list
matrix[0][0] = 100
print("\nAfter changing matrix[0][0] to 100:")
print(matrix)

#==================================================================================
# ITERATING THROUGH LIST
#==================================================================================
"""
NOTES:
- Can use for loop to iterate
- Can use while loop with index
- Can use enumerate() for index and value
"""

# fruits = ["apple", "banana", "cherry"]

# # Using for loop
# print("\nUsing for loop:")
# for fruit in fruits:
#     print(fruit)

# # Using for loop with index
# print("\nUsing range() and len():")
# for i in range(len(fruits)):
#     print(f"Index {i}: {fruits[i]}")

# # Using enumerate()
# print("\nUsing enumerate():")
# for index, fruit in enumerate(fruits):
#     print(f"{index}: {fruit}")

# # Using enumerate() with start parameter
# print("\nUsing enumerate(start=1):")
# for index, fruit in enumerate(fruits, start=1):
#     print(f"{index}. {fruit}")

# # Using while loop
# print("\nUsing while loop:")
# i = 0
# while i < len(fruits):
#     print(fruits[i])
#     i += 1

#==================================================================================
# LIST COMPREHENSION (VERY IMPORTANT)
#==================================================================================
"""
NOTES:
- Concise way to create lists
- Syntax: [expression for item in iterable]
- Can include conditions
"""

# # Basic list comprehension
# squares = [i * i for i in range(1, 6)]
# print("\nSquares using comprehension:", squares)

# # Traditional way (for comparison)
# squares_traditional = []
# for i in range(1, 6):
#     squares_traditional.append(i * i)
# print("Squares using traditional loop:", squares_traditional)

# # List comprehension with condition
# even_numbers = [i for i in range(1, 11) if i % 2 == 0]
# print("\nEven numbers (1-10):", even_numbers)

# # Odd numbers
# odd_numbers = [i for i in range(1, 11) if i % 2 != 0]
# print("Odd numbers (1-10):", odd_numbers)

# # Squares of even numbers
# even_squares = [i * i for i in range(1, 11) if i % 2 == 0]
# print("Squares of even numbers:", even_squares)

# # Converting to uppercase
# words = ["hello", "world", "python"]
# uppercase = [word.upper() for word in words]
# print("\nOriginal words:", words)
# print("Uppercase words:", uppercase)

#==================================================================================
# LIST WITH RANGE()
#==================================================================================
"""
NOTES:
- range() generates sequence of numbers
- Convert to list using list()
- range(stop), range(start, stop), range(start, stop, step)
"""

# # range(stop)
# numbers1 = list(range(10))
# print("\nrange(10):", numbers1)

# # range(start, stop)
# numbers2 = list(range(1, 11))
# print("range(1, 11):", numbers2)

# # range(start, stop, step)
# numbers3 = list(range(0, 20, 2))
# print("range(0, 20, 2):", numbers3)

# numbers4 = list(range(10, 0, -1))
# print("range(10, 0, -1):", numbers4)

#==================================================================================
# BUILT-IN FUNCTIONS WITH LISTS
#==================================================================================
"""
NOTES:
- len() - length
- sum() - sum of numeric elements
- max() - maximum element
- min() - minimum element
- any() - True if any element is True
- all() - True if all elements are True
"""

nums = [10, 20, 30, 40, 50]
print("\nNumbers list:", nums)
print("Length:", len(nums))
print("Sum:", sum(nums))
print("Maximum:", max(nums))
print("Minimum:", min(nums))

# any() - returns True if any element is True
list1 = [False, False, True, False]
print("\nList1:", list1)
print("any():", any(list1))

list2 = [False, False, False]
print("\nList2:", list2)
print("any():", any(list2))

# all() - returns True if all elements are True
list3 = [True, True, True]
print("\nList3:", list3)
print("all():", all(list3))

list4 = [True, False, True]
print("\nList4:", list4)
print("all():", all(list4))

# Using any() and all() with conditions
nums = [2, 4, 6, 8, 10]
print("\nNumbers:", nums)
print("All even?", all(i % 2 == 0 for i in nums))
print("Any greater than 5?", any(i > 5 for i in nums))

#==================================================================================
# CONVERTING BETWEEN DATA TYPES
#==================================================================================
"""
NOTES:
- Can convert string to list
- Can convert tuple to list
- Can convert set to list
- Can convert list to other types
"""

# String to list
text = "hello"
char_list = list(text)
print("\nString:", text)
print("Converted to list:", char_list)

# Tuple to list
my_tuple = (1, 2, 3, 4, 5)
list_from_tuple = list(my_tuple)
print("\nTuple:", my_tuple)
print("Converted to list:", list_from_tuple)

# Set to list
my_set = {3, 1, 4, 2, 5}
list_from_set = list(my_set)
print("\nSet:", my_set)
print("Converted to list:", list_from_set)

# List to tuple
my_list = [1, 2, 3]
tuple_from_list = tuple(my_list)
print("\nList:", my_list)
print("Converted to tuple:", tuple_from_list)

# List to set (removes duplicates)
list_with_duplicates = [1, 2, 2, 3, 3, 3, 4]
set_from_list = set(list_with_duplicates)
print("\nList with duplicates:", list_with_duplicates)
print("Converted to set:", set_from_list)

#==================================================================================
# REAL-LIFE LIST EXAMPLES
#==================================================================================
"""
NOTES:
- Lists are perfect for ordered collections
- Common in real-world scenarios
"""

# Example 1: Shopping Cart
print("\n--- EXAMPLE 1: SHOPPING CART ---")
cart = ["Milk", "Bread", "Eggs"]
print("Initial cart:", cart)

cart.append("Butter")
print("After adding Butter:", cart)

cart.remove("Bread")
print("After removing Bread:", cart)

print("Items in cart:", len(cart))

# Example 2: To-Do List
print("\n--- EXAMPLE 2: TO-DO LIST ---")
tasks = []
print("Initial tasks:", tasks)

tasks.append("Learn Python")
tasks.append("Practice coding")
tasks.append("Build project")
print("All tasks:", tasks)

completed = tasks.pop(0)
print(f"Completed task: {completed}")
print("Remaining tasks:", tasks)

# Example 3: Student Marks
print("\n--- EXAMPLE 3: STUDENT MARKS ---")
marks = [85, 90, 78, 92, 88]
print("Marks:", marks)

total = sum(marks)
average = total / len(marks)
print(f"Total: {total}")
print(f"Average: {average:.2f}")
print(f"Highest: {max(marks)}")
print(f"Lowest: {min(marks)}")

# Example 4: Attendance List
print("\n--- EXAMPLE 4: ATTENDANCE ---")
students = ["Alice", "Bob", "Charlie", "David"]
present = ["Alice", "Charlie", "David"]

print("Total students:", students)
print("Present students:", present)

for student in students:
    if student in present:
        print(f"{student}: Present")
    else:
        print(f"{student}: Absent")

# Example 5: Menu Items
print("\n--- EXAMPLE 5: RESTAURANT MENU ---")
menu = ["Pizza", "Burger", "Pasta", "Salad"]
print("Menu items:")
for index, item in enumerate(menu, 1):
    print(f"{index}. {item}")

# Example 6: Temperature Readings
print("\n--- EXAMPLE 6: TEMPERATURE READINGS ---")
temperatures = [72, 75, 68, 70, 73, 71, 69]
print("Weekly temperatures:", temperatures)

average_temp = sum(temperatures) / len(temperatures)
print(f"Average temperature: {average_temp:.1f}°F")
print(f"Highest: {max(temperatures)}°F")
print(f"Lowest: {min(temperatures)}°F")

# Example 7: Favorite Numbers
print("\n--- EXAMPLE 7: FAVORITE NUMBERS ---")
favorites = [7, 3, 11, 7, 3, 7, 5]
print("Favorite numbers:", favorites)

unique_favorites = list(set(favorites))
print("Unique favorites:", unique_favorites)

