from flask import Flask, render_template, request
from app_functions.text_manipulations import lowercase, uppercase

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    result = None
    if request.method == 'POST':
        operation = request.form.get('operation')
        text = request.form.get('text')
        if operation == 'lower':
            result = lowercase(text)
        elif operation == 'upper':
            result = uppercase(text)
    return render_template('index.html', result=result)

if __name__ == '__main__':
    app.run()
