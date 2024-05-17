def print_pyramid_pattern(n):
    """Prints a pyramid pattern with n levels."""
    for i in range(n):
        print(' ' * (n - i - 1) + '*' * (2 * i + 1))

# Example usage:
print_pyramid_pattern(5)
