"""
String utility functions
"""

def reverse_string(text):
    """Reverse a string."""
    return text[::-1]

def count_vowels(text):
    """Count vowels in string."""
    vowels = "aeiouAEIOU"
    count = 0
    for char in text:
        if char in vowels:
            count += 1
    return count

def is_palindrome(text):
    """Check if string is palindrome."""
    clean = text.replace(" ", "").lower()
    return clean == clean[::-1]

def to_title_case(text):
    """Convert to title case."""
    return text.title()
