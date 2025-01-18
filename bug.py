def function_with_uncommon_error(x):
    try:
        result = 1 / x
        return result
    except ZeroDivisionError:
        return "Error: Cannot divide by zero"
    except TypeError:
        return "Error: Invalid input type"

# Example usage
print(function_with_uncommon_error(0))  # Output: Error: Cannot divide by zero
print(function_with_uncommon_error(10)) # Output: 0.1
print(function_with_uncommon_error("a")) # Output: Error: Invalid input type