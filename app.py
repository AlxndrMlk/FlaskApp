from flask import Flask, render_template, request
from datetime import datetime

app = Flask(__name__)

@app.route('/')
def index():
    headline = 'Hello, world!'
    date = datetime.now()
    return render_template('index.html', headline=headline, date=date)

@app.route('/details')
def details():
    some_list = ['Janek', 'Dharmal', 'Hila', 'Kurt']
    date = datetime.now()
    month = date.month
    return render_template('details.html', date=date, month=month, names=some_list)

@app.route('/hello', methods=['GET', 'POST'])
def hello():
    if request.method == 'GET':
        return render_template('error.html')
    else:
        name = request.form.get('name')
        return render_template('hello.html', name=name)
