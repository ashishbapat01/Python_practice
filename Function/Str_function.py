def my_str(value):
    """
    Convert a value to its string representation.
    
    Args:
        value: The value to be converted to a string.
        
    Returns:
        str: The string representation of the value.
    """
    if isinstance(value, str):
        # If value is already a string, return it as is
        return value
    elif isinstance(value, (int, float, bool)):
        # If value is integer, float, or boolean, convert it to a string using str()
        return str(value)
    else:
        # For other types, use their __str__() method to get the string representation
        return value.__str__()

# Example usage:
print(my_str(123))          # Output: '123'
print(my_str(3.14))         # Output: '3.14'
print(my_str(True))         # Output: 'True'
print(my_str("Hello"))      # Output: 'Hello'
print(my_str([1, 2, 3]))    # Output: '[1, 2, 3]' (using list's __str__() method)
