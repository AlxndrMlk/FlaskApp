from flask import Flask, render_template
from datetime import datetime

app = Flask(__name__)

@app.route('/')
def index():
    headline = 'Hello, world!'
    date = datetime.now()
    return render_template('index.html', headline=headline, date=date)

@app.route('/details')
def details():
    date = datetime.now()
    month = date.month
    return render_template('details.html', date=date, month=month)
