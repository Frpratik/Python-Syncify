"""
Demo module showing __name__ usage
"""

def greet(name):
    """Greet someone."""
    return f"Hello, {name}!"

def main():
    """Main function for testing."""
    print("Running module tests...")
    print(greet("Alice"))
    print(greet("Bob"))

# This runs only when script executed directly
if __name__ == "__main__":
    print("Module run directly")
    main()
else:
    print("Module imported")
