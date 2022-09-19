from flask import Flask, render_template

app = Flask(__name__)


# blog_post = {
#     'title': 
# }



@app.route('/')
def home():
    return render_template('index.html')


@app.route('/about/')
def about():
    return render_template('index_about.html')