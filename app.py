from flask import Flask, render_template, request
from app_functions.text_manipulations import lowercase, uppercase
from app_functions.math_functions import add, subtract, divide, multiply

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    # Initialize or retrieve previous results and selections
    text_result = None
    math_result = None
    selected_text_operation = None
    selected_math_operation = None

    if request.method == 'POST':
        # Process Text Manipulation Form
        if 'text_submit' in request.form:
            selected_text_operation = request.form.get('operation')
            text = request.form.get('text')
            if selected_text_operation == 'lower':
                text_result = lowercase(text)
            elif selected_text_operation == 'upper':
                text_result = uppercase(text)
        else:
            # Retrieve previous text operation and result
            selected_text_operation = request.form.get('operation', None)
            text_result = request.form.get('text_result', None)

        # Process Math Calculation Form
        if 'math_submit' in request.form:
            selected_math_operation = request.form.get('operation_math')
            input_math1 = request.form.get('input_math1')
            input_math2 = request.form.get('input_math2')
            if input_math1 and input_math2:
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
        else:
            # Retrieve previous math operation and result
            selected_math_operation = request.form.get('operation_math', None)
            math_result = request.form.get('math_result', None)

    return render_template('index.html', 
                           text_result=text_result, 
                           math_result=math_result,
                           selected_text_operation=selected_text_operation,
                           selected_math_operation=selected_math_operation)

if __name__ == '__main__':
    app.run(debug=True)
