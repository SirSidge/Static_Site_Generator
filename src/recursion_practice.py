"""def factorial(n):
    if n <= 1:
        return 1
    return n * factorial(n - 1)

print(factorial(5))"""

"""def sum_natural(n):
    if n <= 1:
        return 1
    return n + sum_natural(n - 1)

print(sum_natural(5))"""

def fibonacci(n):
    if n <= 2:
        return 1
    return fibonacci(n-1) + fibonacci(n-2)

print(fibonacci(2))

