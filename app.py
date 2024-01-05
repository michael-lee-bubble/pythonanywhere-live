from flask import Flask, render_template, request, redirect, url_for, session
from app_functions.text_manipulations import lowercase, uppercase
from app_functions.math_functions import add, subtract, divide, multiply
from dotenv import load_dotenv
load_dotenv()  # This loads the variables from .env
import os


app = Flask(__name__)
app.secret_key = os.environ.get('FLASK_SECRET_KEY', 'default-secret-key')

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        # Process Text Manipulation Form
        if 'text_submit' in request.form:
            selected_text_operation = request.form.get('operation')
            text = request.form.get('text')
            if selected_text_operation == 'lower':
                session['text_result'] = lowercase(text)
            elif selected_text_operation == 'upper':
                session['text_result'] = uppercase(text)
            session['selected_text_operation'] = selected_text_operation

        # Process Math Calculation Form
        if 'math_submit' in request.form:
            selected_math_operation = request.form.get('operation_math')
            input_math1 = request.form.get('input_math1')
            input_math2 = request.form.get('input_math2')
            if input_math1 and input_math2:
                input_math1 = float(input_math1)
                input_math2 = float(input_math2)
                if selected_math_operation == 'add':
                    session['math_result'] = add(input_math1, input_math2)
                elif selected_math_operation == 'subtract':
                    session['math_result'] = subtract(input_math1, input_math2)
                elif selected_math_operation == 'multiply':
                    session['math_result'] = multiply(input_math1, input_math2)
                elif selected_math_operation == 'divide':
                    session['math_result'] = divide(input_math1, input_math2)
            session['selected_math_operation'] = selected_math_operation

        # Redirect to prevent form resubmission
        return redirect(url_for('index'))

    # For a GET request, retrieve results and selections from the session
    text_result = session.get('text_result')
    math_result = session.get('math_result')
    selected_text_operation = session.get('selected_text_operation')
    selected_math_operation = session.get('selected_math_operation')

    return render_template('index.html', 
                           text_result=text_result, 
                           math_result=math_result,
                           selected_text_operation=selected_text_operation,
                           selected_math_operation=selected_math_operation)

@app.route('/python_library')
def python_library():
    # Add your implementation for the /python_library route here
    return render_template('python_library.html')

@app.route('/data_library')
def data_library():
    # Add your implementation for the /data_library route here
    return render_template('data_library.html')

if __name__ == '__main__':
    app.run(debug=True)
