def factorial(n):
    """
    Calculate the factorial of a non-negative integer n.
    
    Parameters:
    n (int): A non-negative integer whose factorial is to be computed
    
    Returns:
    int: Factorial of the input number
    """
    if n < 0:
        raise ValueError("Input must be a non-negative integer")
    elif n == 0 or n == 1:
        return 1
    else:
        result = 1
        for i in range(2, n + 1):
            result *= i
        return result

# Example usage
if __name__ == "__main__":
    number = 5
    print(f"The factorial of {number} is {factorial(number)}")