from flask import Flask, request
import operations

app = Flask(__name__)

@app.route('/add')
def add_page():
    a = int(request.args['a'])
    b = int(request.args['b'])
    result = operations.add(a, b)

    return str(result)
@app.route('/sub')
def sub_page():
    a = int(request.args['a'])
    b = int(request.args['b'])
    result = operations.sub(a, b)
    return str(result)

@app.route('/mult')
def mult_page():
    a = int(request.args['a'])
    b = int(request.args['b'])
    result = operations.mult(a, b)
    return str(result)

@app.route('/div')
def div_page():
    a = int(request.args['a'])
    b = int(request.args['b'])
    result = operations.div(a, b)
    return str(result)