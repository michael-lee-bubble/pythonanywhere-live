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

    if request.method == 'POST':
        if 'text_submit' in request.form:  # Check if text manipulation button was clicked
            selected_text_operation = request.form.get('operation')
            text = request.form.get('text')
            if selected_text_operation == 'lower':
                text_result = lowercase(text)
            elif selected_text_operation == 'upper':
                text_result = uppercase(text)

        elif 'math_submit' in request.form:  # Check if math button was clicked
            selected_math_operation = request.form.get('operation_math')
            input_math1 = float(request.form.get('input_math1'))
            input_math2 = float(request.form.get('input_math2'))
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
