def factorial(n):
    print(f"Calling factorial({n})")
    if n < 0:
        raise ValueError("Negative numbers don't have factorial")
    if n == 0 or n == 1:
        return 1
    return n * factorial(n - 1)


def fibonacci(n):
    print(f"Calling fibonacci({n})")
    if n < 0:
        raise ValueError("Negative index not allowed in fibonacci")
    if n == 0:
        return 0
    if n == 1:
        return 1
    return fibonacci(n - 1) + fibonacci(n - 2)


def power(a, b):
    print(f"Calling power({a}, {b})")
    if b < 0:
        raise ValueError("This implementation doesn't handle negative exponents")
    if b == 0:
        return 1
    return a * power(a, b - 1)


def sum_of_digits(n):
    print(f"Calling sum_of_digits({n})")
    n = abs(n)
    if n == 0:
        return 0
    return (n % 10) + sum_of_digits(n // 10)


def reverse_string(s):
    print(f"Calling reverse_string('{s}')")
    if len(s) <= 1:
        return s
    return reverse_string(s[1:]) + s[0]


# Test calls
if __name__ == "__main__":
    print("Factorial of 5:", factorial(5))
    print("Fibonacci of 6:", fibonacci(6))
    print("Power 2^4:", power(2, 4))
    print("Sum of digits (1234):", sum_of_digits(1234))
    print("Reverse of 'hello':", reverse_string("hello"))
