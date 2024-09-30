#!/usr/bin/env python3

from flask import Flask

app = Flask(__name__)


# Base URL, displays the title of the application
@app.route('/')
def index():
    return '''
    <h1>Python Operations with Flask Routing and Views</h1>
    '''.strip()

# Print String Route prints a string
@app.route('/print/<string:parameter>')
def print_string(parameter):
    print(parameter)
    return f'{parameter}'


# Count Route takes an integer and counts from 0 to that number, displaying each on a new line
@app.route('/count/<int:parameter>')
def count(parameter):
    # Return numbers from 0 to parameter - 1, separated by newlines
    return '\n'.join(str(i) for i in range(parameter)) + '\n'


# Math Operation Route performs a math operation (+, -, *, div, %) on two numbers.
@app.route('/math/<int:num1>/<string:operation>/<int:num2>')
def math(num1, operation, num2):
    if operation == '+':
        result = num1 + num2
    elif operation == '-':
        result = num1 - num2
    elif operation == '*':
        result = num1 * num2
    elif operation == 'div':
        if num2 == 0:
            return 'Error: Division by zero is not allowed.'
        result = num1 / num2
    elif operation == '%':
        if num2 == 0:
            return 'Error: Modulo by zero is not allowed.'
        result = num1 % num2
    else:
        return 'Invalid operation.'
    
    return str(result)


if __name__ == '__main__':
    app.run(port=5555, debug=True)
