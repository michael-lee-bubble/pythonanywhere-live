from flask import Flask, render_template, request
from app_functions.text_manipulations import lowercase, uppercase
from app_functions.math_functions import add, subtract, multiply, divide

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    results = {}
    if request.method == 'POST':
        # Text Manipulation Functions
        if 'lowercase' in request.form:
            text = request.form['input_lowercase']
            results['lowercase'] = lowercase(text)
        elif 'uppercase' in request.form:
            text = request.form['input_uppercase']
            results['uppercase'] = uppercase(text)
        
        # Math Functions
        # Note: Convert inputs to appropriate types (e.g., int or float)
        if 'add' in request.form:
            num1 = float(request.form['input_add1'])
            num2 = float(request.form['input_add2'])
            results['add'] = add(num1, num2)
        # ... Similarly handle subtract, multiply, divide

    return render_template('index.html', results=results)

if __name__ == '__main__':
    app.run(debug=True)
