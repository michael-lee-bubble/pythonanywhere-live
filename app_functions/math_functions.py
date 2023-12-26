import sys

def add(input_1, input_2):
    return input_1 + input_2

def subtract(input_1, input_2):
    return input_1 - input_2

def divide(input_1, input_2):
    if input_2 == 0:
        return "Cannot divide by zero"
    return input_1 / input_2

def multiply(input_1, input_2):
    return input_1 * input_2

if len(sys.argv) == 4:
    operation = sys.argv[1].lower()
    input_1 = float(sys.argv[2])
    input_2 = float(sys.argv[3])

    if operation == 'add':
        print(add(input_1, input_2))
    elif operation == 'subtract':
        print(subtract(input_1, input_2))
    elif operation == 'multiply':
        print(multiply(input_1, input_2))
    elif operation == 'divide':
        print(divide(input_1, input_2))
    else:
        print("Invalid operation. Use 'add', 'subtract', 'multiply', or 'divide'.")
else:
    print("Usage: <operation>(<input_1>, <input_2>)")
