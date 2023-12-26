from flask import Flask, render_template, request
from app_functions.text_manipulations import lowercase, uppercase
from app_functions.math_functions import add, subtract, divide, multiply  # Import math functions

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    text_result = None
    math_result = None

    if request.method == 'POST':
        if 'operation' in request.form:
            operation = request.form.get('operation')
            text = request.form.get('text')
            if operation == 'lower':
                text_result = lowercase(text)
            elif operation == 'upper':
                text_result = uppercase(text)

        elif 'operation_math' in request.form:
            operation_math = request.form.get('operation_math')
            input_math1 = float(request.form.get('input_math1'))
            input_math2 = float(request.form.get('input_math2'))
            if operation_math == 'add':
                math_result = add(input_math1, input_math2)  # Use the imported math function
            elif operation_math == 'subtract':
                math_result = subtract(input_math1, input_math2)  # Use the imported math function
            elif operation_math == 'multiply':
                math_result = multiply(input_math1, input_math2)  # Use the imported math function
            elif operation_math == 'divide':
                math_result = divide(input_math1, input_math2)  # Use the imported math function

    return render_template('index.html', text_result=text_result, math_result=math_result)

if __name__ == '__main__':
    app.run()
