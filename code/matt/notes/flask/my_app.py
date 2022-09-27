from flask import Flask, render_template
import random

app = Flask(__name__)

print("hello class! 🚀")

color = 'red'
colors = ['red', 'green', 'blue']


number = random.randint(0, 100)

# localhost:5000
@app.route('/')
def home():
    return render_template('index.html', color=color)

@app.route('/about/')
def about():
    return render_template('about.html', colors=colors)

@app.route('/contact/')
def contact():
    return render_template('contact.html', number=number)


"""
install

1: pip install flask
2: set the variable (by terminal in use, not operating system)
	windows: set FLASK_APP=<appname>.py
	linux: export FLASK_APP=<appname>.py
	powershell: $env:FLASK_APP="<appname>.py"

3: flask run
"""