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
