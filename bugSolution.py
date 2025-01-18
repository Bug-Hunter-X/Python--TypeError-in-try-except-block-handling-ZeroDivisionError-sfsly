def function_with_uncommon_error_solution(x):
    try:
        # Check for valid input type before the division
        if not isinstance(x, (int, float)):
            return "Error: Invalid input type: Input must be a number"
        result = 1 / x
        return result
    except ZeroDivisionError:
        return "Error: Cannot divide by zero"

#Example Usage
print(function_with_uncommon_error_solution(0))  # Output: Error: Cannot divide by zero
print(function_with_uncommon_error_solution(10)) # Output: 0.1
print(function_with_uncommon_error_solution("a")) # Output: Error: Invalid input type: Input must be a number