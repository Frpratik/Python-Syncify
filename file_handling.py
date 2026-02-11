#==================================================================================
# FILE HANDLING IN PYTHON
#==================================================================================
"""
NOTES:
- File handling allows reading from and writing to files
- Files can store data permanently
- Python provides built-in functions for file operations
- Always close files after use or use 'with' statement
- Common file operations: open, read, write, close
"""

#==================================================================================
# OPENING AND CLOSING FILES
#==================================================================================
"""
NOTES:
- open() function opens a file
- Returns a file object
- Must close file using close() method
- Syntax: file_object = open(filename, mode)
- File modes: 'r' (read), 'w' (write), 'a' (append)
"""

# Basic file opening and closing
print("--- OPENING AND CLOSING FILES ---")

# Creating a file for demonstration
file = open("sample.txt", "w")
file.write("Hello, this is a sample file.\n")
file.write("File handling in Python is easy!")
file.close()
print("File 'sample.txt' created and closed\n")

# Opening and closing file
file = open("sample.txt", "r")
print("File opened")
file.close()
print("File closed\n")

#==================================================================================
# FILE MODES
#==================================================================================
"""
NOTES:
- 'r' - Read mode (default), file must exist
- 'w' - Write mode, creates new file or overwrites existing
- 'a' - Append mode, adds to end of file
- 'r+' - Read and write mode
- 'w+' - Write and read mode
- 'a+' - Append and read mode
"""

#==================================================================================
# READING FILES - read()
#==================================================================================
"""
NOTES:
- read() reads entire file content
- read(n) reads n characters
- Returns string
- File pointer moves to end after reading
"""

print("--- READING FILES - read() ---")

# Reading entire file
file = open("sample.txt", "r")
content = file.read()
print("Entire file content:")
print(content)
file.close()

print()

# Reading specific number of characters
file = open("sample.txt", "r")
first_10_chars = file.read(10)
print("First 10 characters:")
print(first_10_chars)
file.close()

print()

#==================================================================================
# READING FILES - readline()
#==================================================================================
"""
NOTES:
- readline() reads one line at a time
- Returns string including newline character
- Returns empty string when end of file reached
- Can call multiple times to read successive lines
"""

print("--- READING FILES - readline() ---")

file = open("sample.txt", "r")
line1 = file.readline()
print("Line 1:", line1)

line2 = file.readline()
print("Line 2:", line2)

line3 = file.readline()  # Empty if no more lines
print("Line 3:", line3)
file.close()

print()

#==================================================================================
# READING FILES - readlines()
#==================================================================================
"""
NOTES:
- readlines() reads all lines
- Returns list of strings
- Each string is a line including newline
- Useful for processing line by line
"""

print("--- READING FILES - readlines() ---")

file = open("sample.txt", "r")
lines = file.readlines()
print("All lines as list:")
print(lines)
file.close()

print()

# Processing each line
file = open("sample.txt", "r")
lines = file.readlines()
print("Processing each line:")
for i, line in enumerate(lines, 1):
    print(f"Line {i}: {line.strip()}")
file.close()

print()

#==================================================================================
# READING FILES - USING LOOP
#==================================================================================
"""
NOTES:
- Can iterate over file object directly
- More memory efficient for large files
- Automatically reads line by line
"""

print("--- READING FILES - USING LOOP ---")

file = open("sample.txt", "r")
print("Reading using for loop:")
for line in file:
    print(line.strip())
file.close()

print()

#==================================================================================
# WRITING TO FILES - write()
#==================================================================================
"""
NOTES:
- write() writes string to file
- 'w' mode overwrites existing content
- imp ---- once we open a file in "w" mode no matter if we write or not it erases everything from file.
- Returns number of characters written
- Must add newline characters manually
"""

print("--- WRITING TO FILES - write() ---")

# Writing to file (overwrites)
file = open("output.txt", "w")
file.write("This is line 1\n")
file.write("This is line 2\n")
file.write("This is line 3\n")
file.close()
print("Data written to 'output.txt'\n")

# Reading back to verify
file = open("output.txt", "r")
print("Content of 'output.txt':")
print(file.read())
file.close()

print()

# Writing without newline
file = open("output2.txt", "w")
file.write("Hello")
file.write("World")
file.close()

file = open("output2.txt", "r")
print("Content without newlines:")
print(file.read())
file.close()

print()

#==================================================================================
# WRITING TO FILES - writelines()
#==================================================================================
"""
NOTES:
- writelines() writes list of strings
- Does NOT add newlines automatically
- Must include newline in strings if needed
"""

print("--- WRITING TO FILES - writelines() ---")

lines = ["First line\n", "Second line\n", "Third line\n"]
file = open("output3.txt", "w")
file.writelines(lines)
file.close()
print("Lines written using writelines()\n")

# Reading back
file = open("output3.txt", "r")
print("Content:")
print(file.read())
file.close()

print()

#==================================================================================
# APPENDING TO FILES
#==================================================================================
"""
NOTES:
- 'a' mode appends to end of file
- Does not overwrite existing content
- Creates file if doesn't exist
- Useful for logs and adding data
"""

print("--- APPENDING TO FILES ---")

# Creating initial file
file = open("append_test.txt", "w")
file.write("Initial content\n")
file.close()

# Appending to file
file = open("append_test.txt", "a")
file.write("Appended line 1\n")
file.write("Appended line 2\n")
file.close()
print("Data appended to 'append_test.txt'\n")

# Reading to verify
file = open("append_test.txt", "r")
print("Final content:")
print(file.read())
file.close()

print()

#==================================================================================
# WITH STATEMENT (RECOMMENDED)
#==================================================================================
"""
NOTES:
- 'with' statement automatically closes file
- More Pythonic and safer
- No need to call close() explicitly
- File closed even if exception occurs
- Recommended way to handle files
"""

print("--- WITH STATEMENT ---")

# Using with for reading
with open("sample.txt", "r") as file:
    content = file.read()
    print("Reading with 'with' statement:")
    print(content)
# File automatically closed here

print("\nFile closed automatically\n")

# Using with for writing
with open("with_example.txt", "w") as file:
    file.write("Written using with statement\n")
    file.write("File will be auto-closed\n")

print("File written and auto-closed\n")

# Verifying
with open("with_example.txt", "r") as file:
    print("Content:")
    print(file.read())

print()

#==================================================================================
# FILE POINTER POSITION
#==================================================================================
"""
NOTES:
- tell() returns current position in file
- seek(offset) moves to specific position
- seek(0) moves to beginning
"""

print("--- FILE POINTER POSITION ---")

with open("sample.txt", "r") as file:
    print("Initial position:", file.tell())
    
    first_10 = file.read(10)
    print("After reading 10 chars:", file.tell())
    
    # next_20 = file.read(10)
    # print(next_20)
    # print("After reading first then, means 11 to 20 chars:", file.tell())
    
    # Move back to beginning
    file.seek(0)
    print("After seek(0):", file.tell())
    
    # Read again
    content = file.read()
    print("Read from beginning:", content[:20], "...")

print()

#==================================================================================
# CHECKING IF FILE EXISTS
#==================================================================================
"""
NOTES:
- Can use exception handling to check file existence
- FileNotFoundError raised if file doesn't exist in read mode
- Better to handle exceptions than check existence
"""

print("--- CHECKING IF FILE EXISTS ---")

# File exists
try:
    with open("sample.txt", "r") as file:
        print("File 'sample.txt' exists and opened successfully")
except FileNotFoundError:
    print("File not found")

# File doesn't exist
try:
    with open("nonexistent.txt", "r") as file:
        content = file.read()
except FileNotFoundError:
    print("File 'nonexistent.txt' does not exist")

print()

#==================================================================================
# READING AND WRITING NUMBERS
#==================================================================================
"""
NOTES:
- Files store data as text
- Must convert numbers to strings when writing
- Must convert strings to numbers when reading
- TypeError: unsupported operand type(s) for +: 'int' and 'str' -> throws if we try to save int in file
"""

print("--- READING AND WRITING NUMBERS ---")

# Writing numbers
numbers = [10, 20, 30, 40, 50]
with open("numbers.txt", "w") as file:
    for num in numbers:
        file.write(str(num) + "\n")

print("Numbers written to file\n")

# Reading numbers back
with open("numbers.txt", "r") as file:
    print("Reading numbers:")
    for line in file:
        number = int(line.strip())
        print(number, end=" ")

print("\n")

#==================================================================================
# WORKING WITH CSV(comma seprataed values)-LIKE DATA
#==================================================================================
"""
NOTES:
- Can manually handle comma-separated values
- split() method useful for parsing
- join() method useful for creating CSV format
"""

print("--- WORKING WITH CSV-LIKE DATA ---")

# Writing CSV data
students = [
    ["Alice", "25", "A"],
    ["Bob", "30", "B"],
    ["Charlie", "28", "A"]
]

with open("students.csv", "w") as file:
    file.write("Name,Age,Grade\n")  # Header
    for student in students:
        line = ",".join(student) + "\n"
        file.write(line)

print("CSV data written\n")

# Reading CSV data
with open("students.csv", "r") as file:
    print("Reading CSV data:")
    header = file.readline().strip()
    print(f"Header: {header}")
    print()
    
    for line in file:
        data = line.strip().split(",")
        print(f"Name: {data[0]}, Age: {data[1]}, Grade: {data[2]}")

print()

# #==================================================================================
# # BINARY FILES
# #==================================================================================
# """
# NOTES:
# - 'b' suffix for binary mode: 'rb', 'wb', 'ab'
# - Used for non-text files (images, videos, etc.)
# - Reads/writes bytes instead of strings
# """

# print("--- BINARY FILES ---")

# # Writing binary data
# data = b"Binary data example"
# with open("binary_file.bin", "wb") as file:
#     file.write(data)

# print("Binary data written\n")

# # Reading binary data
# with open("binary_file.bin", "rb") as file:
#     binary_content = file.read()
#     print(f"Binary content: {binary_content}")
#     print(f"Decoded: {binary_content.decode()}")

# print()

#==================================================================================
# FILE OPERATIONS - PRACTICAL PATTERNS
#==================================================================================
"""
NOTES:
- Common patterns for file operations
- Error handling with files
- Processing large files efficiently
"""

print("--- PRACTICAL FILE PATTERNS ---")

# Pattern 1: Safe file reading with default
def read_file_safe(filename, default="File not found"):
    """Safely read file with default value."""
    try:
        with open(filename, "r") as file:
            return file.read()
    except FileNotFoundError:
        return default

print("Pattern 1: Safe reading")
print(read_file_safe("sample.txt")[:30], "...")
print(read_file_safe("missing.txt"))

print()

# Pattern 2: Reading file into list
def read_lines_to_list(filename):
    """Read file lines into list, stripping whitespace."""
    try:
        with open(filename, "r") as file:
            return [line.strip() for line in file]
    except FileNotFoundError:
        return []

print("Pattern 2: File to list")
lines = read_lines_to_list("sample.txt")
print(f"Lines: {lines}")

print()

#==================================================================================
# REAL-LIFE FILE HANDLING EXAMPLES
#==================================================================================

# Example 1: Todo List Manager
print("--- EXAMPLE 1: TODO LIST MANAGER ---")

def save_todos(tasks, filename="todos.txt"):
    """Save todo list to file."""
    with open(filename, "w") as file:
        for task in tasks:
            file.write(task + "\n")
    print(f"Saved {len(tasks)} tasks")

def load_todos(filename="todos.txt"):
    """Load todo list from file."""
    try:
        with open(filename, "r") as file:
            return [line.strip() for line in file]
    except FileNotFoundError:
        return []

# Using todo manager
tasks = ["Buy groceries", "Study Python", "Exercise"]
save_todos(tasks)

loaded_tasks = load_todos()
print("Loaded tasks:")
for i, task in enumerate(loaded_tasks, 1):
    print(f"{i}. {task}")

print()

# Example 2: Contact Book
print("--- EXAMPLE 2: CONTACT BOOK ---")

def save_contact(name, phone, email, filename="contacts.txt"):
    """Save contact to file."""
    with open(filename, "a") as file:
        file.write(f"{name}|{phone}|{email}\n")

def load_contacts(filename="contacts.txt"):
    """Load all contacts from file."""
    contacts = []
    try:
        with open(filename, "r") as file:
            for line in file:
                parts = line.strip().split("|")
                if len(parts) == 3:
                    contacts.append({
                        "name": parts[0],
                        "phone": parts[1],
                        "email": parts[2]
                    })
    except FileNotFoundError:
        pass
    return contacts

# Clear previous contacts
with open("contacts.txt", "w") as file:
    pass

# Adding contacts
save_contact("Alice", "123-456-7890", "alice@email.com")
save_contact("Bob", "234-567-8901", "bob@email.com")
save_contact("Charlie", "345-678-9012", "charlie@email.com")

# Loading contacts
contacts = load_contacts()
print("Contacts:")
for contact in contacts:
    print(f"Name: {contact['name']}, Phone: {contact['phone']}, Email: {contact['email']}")

print()

# Example 3: Log File Writer
print("--- EXAMPLE 3: LOG FILE WRITER ---")

from datetime import datetime

def write_log(message, filename="app.log"):
    """Write log message with timestamp."""
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    with open(filename, "a") as file:
        file.write(f"[{timestamp}] {message}\n")

def read_logs(filename="app.log", last_n=None):
    """Read log file, optionally last n lines."""
    try:
        with open(filename, "r") as file:
            lines = file.readlines()
            if last_n:
                return lines[-last_n:]
            return lines
    except FileNotFoundError:
        return []

# Clear previous logs
with open("app.log", "w") as file:
    pass

# Writing logs
write_log("Application started")
write_log("User logged in")
write_log("Processing data")
write_log("Task completed successfully")

# Reading logs
logs = read_logs(last_n=3)
print("Last 3 log entries:")
for log in logs:
    print(log.strip())

print()

# Example 4: Student Grade Manager
print("--- EXAMPLE 4: STUDENT GRADE MANAGER ---")

def save_student_grade(name, marks, filename="grades.txt"):
    """Save student name and marks."""
    with open(filename, "a") as file:
        marks_str = ",".join(map(str, marks))
        file.write(f"{name}:{marks_str}\n")

def load_student_grades(filename="grades.txt"):
    """Load all student grades and calculate averages."""
    students = []
    try:
        with open(filename, "r") as file:
            for line in file:
                parts = line.strip().split(":")
                if len(parts) == 2:
                    name = parts[0]
                    marks = list(map(int, parts[1].split(",")))
                    average = sum(marks) / len(marks)
                    students.append({
                        "name": name,
                        "marks": marks,
                        "average": average
                    })
    except FileNotFoundError:
        pass
    return students

# Clear previous grades
with open("grades.txt", "w") as file:
    pass

# Adding student grades
save_student_grade("Alice", [85, 90, 88, 92])
save_student_grade("Bob", [78, 82, 80, 85])
save_student_grade("Charlie", [92, 95, 90, 93])

# Loading and displaying grades
students = load_student_grades()
print("Student Grades:")
for student in students:
    print(f"{student['name']}: {student['marks']} -> Average: {student['average']:.2f}")

print()

# Example 5: Configuration File Handler
print("--- EXAMPLE 5: CONFIGURATION FILE ---")

def save_config(config_dict, filename="config.txt"):
    """Save configuration as key=value pairs."""
    with open(filename, "w") as file:
        for key, value in config_dict.items():
            file.write(f"{key}={value}\n")

def load_config(filename="config.txt"):
    """Load configuration from file."""
    config = {}
    try:
        with open(filename, "r") as file:
            for line in file:
                line = line.strip()
                if "=" in line:
                    key, value = line.split("=", 1)
                    config[key] = value
    except FileNotFoundError:
        pass
    return config

# Saving configuration
config = {
    "theme": "dark",
    "language": "English",
    "auto_save": "true",
    "font_size": "12"
}
save_config(config)
print("Configuration saved")

# Loading configuration
loaded_config = load_config()
print("Loaded configuration:")
for key, value in loaded_config.items():
    print(f"  {key}: {value}")

print()

# Example 6: Word Counter
print("--- EXAMPLE 6: WORD COUNTER ---")

def count_words_in_file(filename):
    """Count words in a file."""
    try:
        with open(filename, "r") as file:
            content = file.read()
            words = content.split()
            return len(words)
    except FileNotFoundError:
        return 0

def count_lines_in_file(filename):
    """Count lines in a file."""
    try:
        with open(filename, "r") as file:
            return len(file.readlines())
    except FileNotFoundError:
        return 0

# Creating sample file
with open("story.txt", "w") as file:
    file.write("Once upon a time in a faraway land.\n")
    file.write("There lived a brave knight.\n")
    file.write("The knight went on many adventures.\n")

word_count = count_words_in_file("story.txt")
line_count = count_lines_in_file("story.txt")
print(f"File statistics for 'story.txt':")
print(f"  Lines: {line_count}")
print(f"  Words: {word_count}")

print()

# Example 7: File Backup
print("--- EXAMPLE 7: FILE BACKUP ---")

def backup_file(source, backup_suffix=".backup"):
    """Create backup of file."""
    try:
        with open(source, "r") as file:
            content = file.read()
        
        backup_name = source + backup_suffix
        with open(backup_name, "w") as file:
            file.write(content)
        
        return True, f"Backup created: {backup_name}"
    except FileNotFoundError:
        return False, f"Source file '{source}' not found"

# Creating backup
success, message = backup_file("sample.txt")
print(message)

# Verifying backup
if success:
    with open("sample.txt.backup", "r") as file:
        print("Backup content preview:")
        print(file.read()[:50], "...")

print()

# Example 8: Data Export/Import
print("--- EXAMPLE 8: DATA EXPORT/IMPORT ---")

def export_data(data, filename="export.txt"):
    """Export list of dictionaries to file."""
    with open(filename, "w") as file:
        # Write header
        if data:
            keys = data[0].keys()
            file.write(",".join(keys) + "\n")
            
            # Write data
            for item in data:
                values = [str(item[key]) for key in keys]
                file.write(",".join(values) + "\n")

def import_data(filename="export.txt"):
    """Import data from file to list of dictionaries."""
    data = []
    try:
        with open(filename, "r") as file:
            lines = file.readlines()
            if not lines:
                return data
            
            # Parse header
            keys = lines[0].strip().split(",")
            
            # Parse data
            for line in lines[1:]:
                values = line.strip().split(",")
                item = dict(zip(keys, values))
                data.append(item)
    except FileNotFoundError:
        pass
    return data

# Exporting data
products = [
    {"id": "1", "name": "Laptop", "price": "999"},
    {"id": "2", "name": "Mouse", "price": "25"},
    {"id": "3", "name": "Keyboard", "price": "79"}
]
export_data(products, "products.txt")
print("Data exported to 'products.txt'")

# Importing data
imported = import_data("products.txt")
print("\nImported data:")
for product in imported:
    print(f"  ID: {product['id']}, Name: {product['name']}, Price: ${product['price']}")

print()

# Example 9: File Search
print("--- EXAMPLE 9: SEARCH IN FILE ---")

def search_in_file(filename, search_term):
    """Search for term in file and return matching lines."""
    matches = []
    try:
        with open(filename, "r") as file:
            for line_num, line in enumerate(file, 1):
                if search_term.lower() in line.lower():
                    matches.append((line_num, line.strip()))
    except FileNotFoundError:
        pass
    return matches

# Creating search file
with open("search_demo.txt", "w") as file:
    file.write("Python is a great programming language.\n")
    file.write("JavaScript is also popular.\n")
    file.write("Python is easy to learn.\n")
    file.write("Many developers love Python.\n")

# Searching
results = search_in_file("search_demo.txt", "python")
print(f"Search results for 'python':")
for line_num, line in results:
    print(f"  Line {line_num}: {line}")

print()

# Example 10: File Statistics
print("--- EXAMPLE 10: FILE STATISTICS ---")

def get_file_stats(filename):
    """Get comprehensive file statistics."""
    stats = {
        "lines": 0,
        "words": 0,
        "characters": 0,
        "characters_no_spaces": 0
    }
    
    try:
        with open(filename, "r") as file:
            for line in file:
                stats["lines"] += 1
                stats["words"] += len(line.split())
                stats["characters"] += len(line)
                stats["characters_no_spaces"] += len(line.replace(" ", ""))
    except FileNotFoundError:
        return None
    
    return stats

# Getting stats
stats = get_file_stats("sample.txt")
if stats:
    print("File statistics for 'sample.txt':")
    print(f"  Lines: {stats['lines']}")
    print(f"  Words: {stats['words']}")
    print(f"  Characters (with spaces): {stats['characters']}")
    print(f"  Characters (without spaces): {stats['characters_no_spaces']}")

print("\n" + "="*80)
print("END OF FILE HANDLING TUTORIAL")
print("="*80)