import sys

def lowercase(text):
    return text.lower()

def uppercase(text):
    return text.upper()

# Check if arguments were provided
if len(sys.argv) > 2:
    operation = sys.argv[1].lower()
    user_input = sys.argv[2]

    if operation == 'lower':
        print(lowercase(user_input))
    elif operation == 'upper':
        print(uppercase(user_input))
    else:
        print("First argument must be 'lower' or 'upper'.")

else:
    print("Please provide two arguments: the operation ('lower' or 'upper') and the text.")