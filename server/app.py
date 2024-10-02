#!/usr/bin/env python3

from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return '<h1>Python Operations with Flask Routing and Views</h1>'

@app.route('/print/parameter')
def print_string(parameter):
    return f'my name {parameter}'

@app.route('/count/parameter')
def count(parameter):
    numbers = '<br>'.join (str(i) for i in range(1, parameter + 1))
    return numbers 

@app.route('/math/<num1>/<operation>/<num2>')
def math(num1, operation, num2):
    if operation  == '+':
        result = num1 + num2
    elif operation == '-':
        result = num1 - num2
    elif operation == '*':
        result = num1 * num2

    elif operation == 'div':
        if num2 != 0:
            result = num1 / num2 
        else:
            return 'Error: Division by zero'
    return f'The result of {num1} {operation} {num2} is {result}'




if __name__ == '__main__':
    app.run(port=5555, debug=True)
