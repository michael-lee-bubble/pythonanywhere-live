from flask import Flask, render_template, request
from app_functions.text_manipulations import lowercase, uppercase
from app_functions.math_functions import add, subtract, divide, multiply  # Import math functions

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    text_result = None
    math_result = None
    selected_text_operation = None
    selected_math_operation = None

    # Check for existing session data (if you're using sessions to store previous state)
    # If not using sessions, you can initialize these to default values or based on some other logic

    if request.method == 'POST':
        # Text Manipulation Section
        selected_text_operation = request.form.get('operation', selected_text_operation)
        text = request.form.get('text', None)
        if 'text_submit' in request.form:
            if selected_text_operation == 'lower':
                text_result = lowercase(text)
            elif selected_text_operation == 'upper':
                text_result = uppercase(text)

        # Math Calculation Section
        selected_math_operation = request.form.get('operation_math', selected_math_operation)
        input_math1 = request.form.get('input_math1', None)
        input_math2 = request.form.get('input_math2', None)
        if 'math_submit' in request.form:
            if input_math1 and input_math2:  # Ensure that both inputs are provided
                input_math1 = float(input_math1)
                input_math2 = float(input_math2)
                if selected_math_operation == 'add':
                    math_result = add(input_math1, input_math2)
                elif selected_math_operation == 'subtract':
                    math_result = subtract(input_math1, input_math2)
                elif selected_math_operation == 'multiply':
                    math_result = multiply(input_math1, input_math2)
                elif selected_math_operation == 'divide':
                    math_result = divide(input_math1, input_math2)

    return render_template('index.html', 
                           text_result=text_result, 
                           math_result=math_result,
                           selected_text_operation=selected_text_operation,
                           selected_math_operation=selected_math_operation)

if __name__ == '__main__':
    app.run()
