# test_division.py
a = 10
b = 2# change this to 0 to simulate a failure

try:
    result = a / b
    print(f"Result: {result}")
except ZeroDivisionError as e:
    print(f"Error: {e}")
    exit(1)  # Tell Jenkins to mark build as FAILED

