# Even or Odd Checker
def check_even_odd(num):
    return "Even" if num % 2 == 0 else "Odd"

print(check_even_odd(7))

# Simple Calculator
def calculator(a, b, op):
    if op == '+': return a + b
    elif op == '-': return a - b
    elif op == '*': return a * b
    elif op == '/': return a / b
    else: return "Invalid operator"

print(calculator(10, 5, '*'))

# Word Counter
def word_count(text):
    return len(text.split())

print(word_count("AI Engineer journey has started"))
