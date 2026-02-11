#==================================================================================
# DATA TYPES IN PYTHON - OVERVIEW
#==================================================================================
"""
NOTES:
- Python has several built-in data types for different kinds of values
- Data types determine what operations can be performed on the data
- Python is dynamically typed (types are inferred, not declared)
- Use type() function to check data type of any value
"""

#==================================================================================
# 1. NUMERIC TYPES
#==================================================================================
"""
int → integer numbers (whole numbers without decimals)
    Examples: 10, -5, 0, 1000
    See int.py for detailed examples

float → floating-point numbers (decimals)
    Examples: 3.14, -0.5, 2.0
    See float.py for detailed examples

complex → complex numbers (with real and imaginary parts)
    Examples: 2 + 3j, 5 - 4j
    Format: a + bj (where j is the imaginary unit)
    See complex.py for detailed examples
"""

#==================================================================================
# 2. BOOLEAN TYPE
#==================================================================================
"""
bool → boolean values (True or False)
    Only two possible values: True or False
    Used in conditional statements and comparisons
    See boolean.py for detailed examples
"""

#==================================================================================
# 3. TEXT TYPE
#==================================================================================
"""
str → string (sequence of characters/text)
    Examples: "Hello", 'Python', "123"
    Can use single or double quotes
    See string.py for detailed examples
"""

#==================================================================================
# 4. SEQUENCE TYPES
#==================================================================================
"""
list → ordered, mutable, changeable collection
    Examples: [1, 2, 3], ["a", "b"], [1, "mixed", 3.14]
    Allow duplicate values
    Use square brackets []
    See list.py for detailed examples

tuple → ordered, immutable, unchangeable collection
    Examples: (1, 2, 3), ("a", "b"), (1, "mixed", 3.14)
    Allow duplicate values
    Use parentheses ()
    More memory efficient than lists
    See tuple.py for detailed examples

range → sequence of numbers
    Examples: range(5), range(1, 10), range(0, 10, 2)
    Used mainly in loops
    Immutable sequence type
"""

#==================================================================================
# 5. SET TYPES
#==================================================================================
"""
set → unordered, mutable, collection of unique values
    Examples: {1, 2, 3}, {"a", "b"}
    No duplicate values allowed
    No indexing or slicing
    Use curly braces {}
    See set.py for detailed examples

frozenset → unordered, immutable set of unique values
    Similar to set but cannot be modified after creation
"""

#==================================================================================
# 6. MAPPING TYPE
#==================================================================================
"""
dict → unordered collection of key-value pairs
    Examples: {"name": "Alice", "age": 25}
    Keys must be unique and immutable
    Values can be any data type
    Use curly braces {} with key:value pairs
    Fast lookup by key
    See dict.py for detailed examples
"""

#==================================================================================
# 7. OTHER TYPES
#==================================================================================
"""
None → represents absence of value or null
    Used to indicate missing or undefined value
    Only one instance of None

bytes → immutable sequence of bytes
    Used for binary data
    Created with b prefix: b"hello"

bytearray → mutable sequence of bytes
    Similar to bytes but can be modified

memoryview → memory view object
    Provides access to internal data of objects
"""

#==================================================================================
# TYPE CHECKING
#==================================================================================
"""
Use type() function to check data type of a value:
    type(10)              # <class 'int'>
    type(3.14)            # <class 'float'>
    type("hello")         # <class 'str'>
    type([1, 2, 3])       # <class 'list'>
    type((1, 2, 3))       # <class 'tuple'>
    type({1, 2, 3})       # <class 'set'>
    type({"a": 1})        # <class 'dict'>
    type(True)            # <class 'bool'>
    type(2+3j)            # <class 'complex'>
    type(None)            # <class 'NoneType'>

Use isinstance() to check if value is of a specific type:
    isinstance(10, int)           # True
    isinstance(3.14, float)       # True
    isinstance("hello", str)      # True
    isinstance([1, 2], list)      # True
"""

#==================================================================================
# QUICK REFERENCE - FILE GUIDE
#==================================================================================
"""
For detailed examples and operations on each data type, see:

NUMERIC TYPES:
  - int.py             → Integer operations and conversions
  - float.py           → Float operations, rounding, conversions
  - complex.py         → Complex numbers with real and imaginary parts

TEXT & BOOLEAN:
  - string.py          → String creation, methods, slicing, formatting
  - boolean.py         → Boolean values, comparisons, logical operations

SEQUENCE TYPES:
  - list.py            → List creation, methods, operations, comprehensions
  - tuple.py           → Tuple creation, unpacking, use cases
  - set.py             → Set creation, operations, union/intersection

MAPPING TYPE:
  - dict.py            → Dictionary creation, methods, operations

OTHER:
  - data_types.py      → This file (overview of all types)
"""
