def compute_division(a, b):
    try:
        result = a / b
        return result
    except ZeroDivisionError:
        print("Error: Division by zero occurred!")
        return None

result = compute_division(5, 0)
if result is not None:
    print("Result of division:", result)