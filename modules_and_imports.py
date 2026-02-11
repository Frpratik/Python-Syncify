#==================================================================================
# MODULES AND IMPORTS IN PYTHON
#==================================================================================
"""
NOTES:
- Module is a file containing Python code (functions, classes, variables)
- Modules help organize code into separate files
- Modules promote code reusability
- Python has many built-in modules
- Can create custom modules
- Use 'import' statement to use modules
"""

#==================================================================================
# WHAT ARE MODULES?
#==================================================================================
"""
NOTES:
- Module = Python file (.py)
- Contains reusable code
- Examples: math, random, datetime
- Helps break large programs into smaller parts
- Makes code maintainable and organized
"""

print("--- WHAT ARE MODULES? ---")
print("Module is a Python file containing code")
print("Modules help organize and reuse code")
print("Python provides many built-in modules\n")

#==================================================================================
# IMPORTING MODULES - BASIC
#==================================================================================
"""
NOTES:
- import module_name imports entire module
- Access using module_name.function_name
- Module loaded once, can use multiple times
"""

print("--- BASIC IMPORT ---")

# Importing math module
import math

print("Using math module:")
print(f"Square root of 16: {math.sqrt(16)}")
print(f"Value of pi: {math.pi}")
print(f"5 to power 3: {math.pow(5, 3)}")
print()

# Importing random module
import random

print("Using random module:")
print(f"Random number (0-1): {random.random()}")
print(f"Random integer (1-10): {random.randint(1, 10)}")
print()

#==================================================================================
# IMPORTING SPECIFIC ITEMS - FROM...IMPORT
#==================================================================================
"""
NOTES:
- from module import item imports specific item
- Can use item directly without module name
- More convenient for frequently used items
- Can import multiple items
"""

print("--- FROM...IMPORT ---")

# Importing specific function
from math import sqrt, pi

print("Direct access without module name:")
print(f"Square root of 25: {sqrt(25)}")
print(f"Value of pi: {pi}")
print()

# Importing multiple items
from random import randint, choice

print("Using imported items directly:")
print(f"Random integer: {randint(1, 100)}")
colors = ["red", "green", "blue"]
print(f"Random choice: {choice(colors)}")
print()

#==================================================================================
# IMPORTING WITH ALIAS
#==================================================================================
"""
NOTES:
- 'as' keyword creates alias (nickname)
- Makes long module names shorter
- Common convention for some modules
- Example: pandas as pd, numpy as np
"""

print("--- IMPORTING WITH ALIAS ---")

# Alias for module
import datetime as dt

print("Using alias 'dt' for datetime:")
now = dt.datetime.now()
print(f"Current date and time: {now}")
print()

# Alias for specific item
from math import factorial as fact

print("Using alias 'fact' for factorial:")
print(f"Factorial of 5: {fact(5)}")
print()

#==================================================================================
# IMPORTING EVERYTHING - IMPORT *
#==================================================================================
"""
NOTES:
- from module import * imports everything
- NOT RECOMMENDED (can cause name conflicts)
- Makes code less readable
- Use only in interactive sessions
"""

print("--- IMPORT * (NOT RECOMMENDED) ---")

from math import *

print("All math functions available directly:")
print(f"sqrt(16): {sqrt(16)}")
print(f"ceil(4.3): {ceil(4.3)}")
print(f"floor(4.7): {floor(4.7)}")
print("(Better to import specific items)\n")

#==================================================================================
# MATH MODULE
#==================================================================================
"""
NOTES:
- Provides mathematical functions
- Common functions: sqrt, pow, ceil, floor, factorial
- Constants: pi, e
- Trigonometric functions: sin, cos, tan
"""

print("--- MATH MODULE ---")

import math

print("Math module functions:")
print(f"sqrt(144): {math.sqrt(144)}")
print(f"pow(2, 8): {math.pow(2, 8)}")
print(f"factorial(5): {math.factorial(5)}")
print(f"ceil(4.2): {math.ceil(4.2)}")
print(f"floor(4.8): {math.floor(4.8)}")
print()

print("Math constants:")
print(f"pi: {math.pi}")
print(f"e: {math.e}")
print()

#only for knowledge
# print("Trigonometric functions:")
# print(f"sin(0): {math.sin(0)}")
# print(f"cos(0): {math.cos(0)}")
# print(f"degrees(3.14159): {math.degrees(3.14159)}")
# print(f"radians(180): {math.radians(180)}")
# print()

#==================================================================================
# RANDOM MODULE
#==================================================================================
"""
NOTES:
- Generate random numbers
- random() - float between 0 and 1
- randint(a, b) - integer between a and b (inclusive)
- choice(sequence) - random element from sequence
- shuffle(list) - shuffle list in place
- sample(sequence, k) - k random elements
"""

print("--- RANDOM MODULE ---")

import random

print("Random number generation:")
print(f"random(): {random.random()}")
print(f"random(): {random.random()}")
print()

print("Random integers:")
print(f"randint(1, 10): {random.randint(1, 10)}")
print(f"randint(1, 10): {random.randint(1, 10)}")
print(f"randint(100, 200): {random.randint(100, 200)}")
print()

print("Random choice:")
fruits = ["apple", "banana", "cherry", "date"]
print(f"Fruits: {fruits}")
print(f"Random fruit: {random.choice(fruits)}")
print(f"Random fruit: {random.choice(fruits)}")
print()

print("Random sample (multiple items):")
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(f"Numbers: {numbers}")
print(f"3 random numbers: {random.sample(numbers, 3)}")
print()

print("Shuffle list:")
deck = ["A", "K", "Q", "J", "10"]
print(f"Original: {deck}")
random.shuffle(deck)
print(f"Shuffled: {deck}")
print()

# print("Random with range:")
# print(f"uniform(1, 10): {random.uniform(1, 10)}")
# print(f"uniform(1, 10): {random.uniform(1, 10)}")
# print()

#==================================================================================
# DATETIME MODULE
#==================================================================================
"""
NOTES:
- Work with dates and times
- datetime.datetime - date and time combined
- datetime.date - just date
- datetime.time - just time
- timedelta - difference between dates
"""

print("--- DATETIME MODULE ---")

import datetime

print("Current date and time:")
now = datetime.datetime.now()
print(f"Now: {now}")
print(f"Year: {now.year}")
print(f"Month: {now.month}")
print(f"Day: {now.day}")
print(f"Hour: {now.hour}")
print(f"Minute: {now.minute}")
print(f"Second: {now.second}")
print()

print("Current date only:")
today = datetime.date.today()
print(f"Today: {today}")
print()

print("Creating specific date:")
birthday = datetime.date(1990, 5, 15)
print(f"Birthday: {birthday}")
print()

print("Creating specific datetime:")
meeting = datetime.datetime(2025, 12, 25, 14, 30)
print(f"Meeting: {meeting}")
print()

print("Formatting dates:")
print(f"Formatted: {now.strftime('%Y-%m-%d')}")
print(f"Formatted: {now.strftime('%d/%m/%Y')}")
print(f"Formatted: {now.strftime('%B %d, %Y')}")
print(f"Formatted: {now.strftime('%I:%M %p')}")
print()

print("Date arithmetic:")
today = datetime.date.today()
one_week = datetime.timedelta(days=7)
next_week = today + one_week
print(f"Today: {today}")
print(f"Next week: {next_week}")

last_month = today - datetime.timedelta(days=30)
print(f"30 days ago: {last_month}")
print()

# #==================================================================================
# # OS MODULE
# #==================================================================================
# """
# NOTES:
# - Interact with operating system
# - File and directory operations
# - Environment variables
# - Path operations
# """

# print("--- OS MODULE ---")

# import os

# print("Operating system information:")
# print(f"OS name: {os.name}")
# print(f"Current directory: {os.getcwd()}")
# print()

# print("Environment variables (sample):")
# # Get HOME or USERPROFILE (works on both Unix and Windows)
# home = os.environ.get('HOME') or os.environ.get('USERPROFILE')
# print(f"Home directory: {home}")
# print()

# print("Path operations:")
# path = "/folder/subfolder/file.txt"
# print(f"Path: {path}")
# print(f"Directory name: {os.path.dirname(path)}")
# print(f"Base name: {os.path.basename(path)}")
# print(f"File extension: {os.path.splitext(path)[1]}")
# print()

# print("Checking file/directory existence:")
# print(f"Does 'sample.txt' exist? {os.path.exists('sample.txt')}")
# print()

# print("Joining paths:")
# joined_path = os.path.join("folder", "subfolder", "file.txt")
# print(f"Joined path: {joined_path}")
# print()

# #==================================================================================
# # SYS MODULE
# #==================================================================================
# """
# NOTES:
# - System-specific parameters
# - Command-line arguments
# - Python version information
# - Exit program
# """

# print("--- SYS MODULE ---")

# import sys

# print("Python information:")
# print(f"Python version: {sys.version}")
# print(f"Python version info: {sys.version_info}")
# print(f"Platform: {sys.platform}")
# print()

# print("Path where Python looks for modules:")
# print(f"Number of paths: {len(sys.path)}")
# print(f"First path: {sys.path[0]}")
# print()

# # Command line arguments (empty in script execution)
# print("Command line arguments:")
# print(f"Script name: {sys.argv[0]}")
# print(f"All arguments: {sys.argv}")
# print()

# #==================================================================================
# # TIME MODULE
# #==================================================================================
# """
# NOTES:
# - Time-related functions
# - Sleep (pause execution)
# - Measure time
# - Time formatting
# """

# print("--- TIME MODULE ---")

# import time

# print("Current time (timestamp):")
# current_time = time.time()
# print(f"Timestamp: {current_time}")
# print()

# print("Sleep (pause) example:")
# print("Pausing for 1 second...")
# time.sleep(1)
# print("Resumed!")
# print()

# print("Measuring execution time:")
# start_time = time.time()

# # Some operation
# total = 0
# for i in range(1000000):
#     total += i

# end_time = time.time()
# elapsed = end_time - start_time
# print(f"Time taken: {elapsed:.4f} seconds")
# print()

# print("Formatted time:")
# current = time.localtime()
# formatted = time.strftime("%Y-%m-%d %H:%M:%S", current)
# print(f"Current time: {formatted}")
# print()

# #==================================================================================
# # STATISTICS MODULE
# #==================================================================================
# """
# NOTES:
# - Statistical functions
# - Mean, median, mode
# - Standard deviation, variance
# """

# print("--- STATISTICS MODULE ---")

# import statistics

# data = [10, 20, 30, 40, 50, 60, 70]
# print(f"Data: {data}")
# print()

# print("Statistical measures:")
# print(f"Mean (average): {statistics.mean(data)}")
# print(f"Median (middle): {statistics.median(data)}")
# print(f"Mode (most common): {statistics.mode([1, 2, 2, 3, 3, 3, 4])}")
# print(f"Standard deviation: {statistics.stdev(data):.2f}")
# print(f"Variance: {statistics.variance(data):.2f}")
# print()

#==================================================================================
# CREATING YOUR OWN MODULE
#==================================================================================
"""
NOTES:
- Any Python file can be a module
- Save functions in a .py file
- Import using filename (without .py)
- Module name should be valid identifier
"""

print("--- CREATING YOUR OWN MODULE ---")

# Importing custom module
import my_math

print("Using custom module:")
print(f"add(10, 5): {my_math.add(10, 5)}")
print(f"subtract(10, 5): {my_math.subtract(10, 5)}")
print(f"multiply(10, 5): {my_math.multiply(10, 5)}")
print(f"divide(10, 5): {my_math.divide(10, 5)}")
print(f"PI constant: {my_math.PI}")
print()

#==================================================================================
# CREATING MODULE WITH MULTIPLE FUNCTIONS
#==================================================================================
"""
NOTES:
- Modules can contain multiple related functions
- Group related functionality together
- Good for code organization
"""

print("--- MODULE WITH MULTIPLE FUNCTIONS ---")

# Using the module
import string_utils

print("\nUsing string utilities:")
text = "Hello World"
print(f"Original: {text}")
print(f"Reversed: {string_utils.reverse_string(text)}")
print(f"Vowel count: {string_utils.count_vowels(text)}")
print(f"Is palindrome: {string_utils.is_palindrome(text)}")
print(f"Title case: {string_utils.to_title_case('hello world')}")
print()
#==================================================================================
# REAL-LIFE MODULE USAGE EXAMPLES
#==================================================================================

# Example 1: Password Generator
print("--- EXAMPLE 1: PASSWORD GENERATOR ---")

import random
import string

def generate_password(length=12):
    """Generate random password."""
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for _ in range(length))
    return password

print("Generated passwords:")
for i in range(3):
    print(f"Password {i+1}: {generate_password()}")
print()

# Example 2: File Timestamp Logger
print("--- EXAMPLE 2: FILE TIMESTAMP LOGGER ---")

import datetime

def log_message(message, filename="log.txt"):
    """Log message with timestamp."""
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    log_entry = f"[{timestamp}] {message}\n"
    
    with open(filename, "a") as f:
        f.write(log_entry)
    
    return log_entry

# Clear previous log
with open("log.txt", "w") as f:
    pass

print("Logging messages:")
print(log_message("Application started"))
print(log_message("User logged in"))
print(log_message("Processing complete"))
print()

# Example 3: Random Quiz Generator
print("--- EXAMPLE 3: RANDOM QUIZ GENERATOR ---")

import random

questions_db = [
    {"question": "What is 2 + 2?", "answer": "4"},
    {"question": "Capital of France?", "answer": "Paris"},
    {"question": "Python was created by?", "answer": "Guido van Rossum"},
    {"question": "What is 5 * 5?", "answer": "25"},
    {"question": "Largest ocean?", "answer": "Pacific"}
]

def generate_quiz(num_questions=3):
    """Generate random quiz questions."""
    selected = random.sample(questions_db, min(num_questions, len(questions_db)))
    return selected

quiz = generate_quiz(3)
print("Random quiz generated:")
for i, q in enumerate(quiz, 1):
    print(f"{i}. {q['question']}")
print()

# Example 4: Random Team Generator
print("--- EXAMPLE 6: RANDOM TEAM GENERATOR ---")

import random

def create_teams(players, num_teams=2):
    """Randomly divide players into teams."""
    shuffled = players.copy()
    random.shuffle(shuffled)
    
    team_size = len(shuffled) // num_teams
    teams = []
    
    for i in range(num_teams):
        start = i * team_size
        end = start + team_size if i < num_teams - 1 else len(shuffled)
        teams.append(shuffled[start:end])
    
    return teams

players = ["Alice", "Bob", "Charlie", "David", "Eve", "Frank"]
teams = create_teams(players, 2)

print("Random teams:")
for i, team in enumerate(teams, 1):
    print(f"Team {i}: {', '.join(team)}")
print()

# Example 5: Date Calculator
print("--- EXAMPLE 7: DATE CALCULATOR ---")

import datetime

def days_until_date(target_date):
    """Calculate days until target date."""
    today = datetime.date.today()
    delta = target_date - today
    return delta.days

def add_business_days(start_date, days):
    """Add business days (excluding weekends)."""
    current = start_date
    added = 0
    
    while added < days:
        current += datetime.timedelta(days=1)
        # 5 = Saturday, 6 = Sunday
        if current.weekday() < 5:
            added += 1
    
    return current

# Days until New Year
new_year = datetime.date(2026, 1, 1)
days = days_until_date(new_year)
print(f"Days until New Year 2026: {days}")

# Add business days
today = datetime.date.today()
future = add_business_days(today, 10)
print(f"10 business days from {today}: {future}")
print()

# Example 6: Timer Decorator
print("--- EXAMPLE 9: EXECUTION TIMER ---")

import time

def measure_time(func, *args):
    """Measure function execution time."""
    start = time.time()
    result = func(*args)
    end = time.time()
    elapsed = end - start
    return result, elapsed

def slow_function(n):
    """Simulate slow operation."""
    total = 0
    for i in range(n):
        total += i
    return total

result, time_taken = measure_time(slow_function, 1000000)
print(f"Function result: {result}")
print(f"Time taken: {time_taken:.4f} seconds")
print()
