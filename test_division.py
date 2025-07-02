# test_division.py
a = 10
b = 0

try:
    result = a / b
    print(f"Result: {result}")
except ZeroDivisionError as e:
    print(f"Error: {e}")
    exit(1)  # Tell Jenkins to mark build as FAILED

