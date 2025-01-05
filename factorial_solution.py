def factorial(n):
    if n < 0:
        return None  # or raise ValueError("Factorial is not defined for negative numbers.")
    elif n == 0:
        return 1
    else:
        return n * factorial(n-1)

print(factorial(5))
print(factorial(-1))