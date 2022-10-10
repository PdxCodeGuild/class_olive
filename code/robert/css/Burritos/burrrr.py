from flask import Flask, render_template

app = Flask(__name__)

tortilla = ['Wheat','Spicy','Gluten Free','Blue Corn']
toppings = ['onions','lettuce','cheese']
salsa = ['bebita', 'spicalita', 'te queiro dolor']
meats = ['soy','pollo','carne asada','al pastor']

@app.route('/')
def home():
    return render_template('index.html', tortilla = tortilla, toppings = toppings, salsa = salsa, meats=meats)

