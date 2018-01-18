from __future__ import division
from flask import Flask #don't forget localhost:5000
from flask import render_template
app = Flask(__name__) #

@app.route('/')
def index():
    return render_template('bootDic.html', name = {'david': 68, 'monicas': 62, 'hector': 100})


# @app.route('/')
# def index():
#     return render_template('bootDic.html', name = ["monica","david","hector"])

@app.route('/add/<int:num1>/<int:num2>')
def add(num1, num2):
    return '{} + {} = {}'.format(num1, num2, float(num1 + num2))

@app.route('/substract/<int:num1>/<int:num2>')
def substract(num1, num2):
    return '{} - {} = {}'.format(num1, num2, float(num1 - num2))

@app.route('/divide/<int:num1>/<int:num2>')
def divide(num1, num2):
    return '{} / {} = {}'.format(num1, num2, float(num1 / num2))

@app.route('/multiply/<int:num1>/<int:num2>')
def multiply(num1, num2):
    return '{} x {} = {}'.format(num1, num2, float(num1 * num2))

if __name__ == "__main__":
	app.run(debug=True)
