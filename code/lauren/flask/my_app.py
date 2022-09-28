from flask import Flask, render_template

app = Flask(__name__)

posts = [
    {
        'title': "Foods you'll slap your mother for",
        'author': "Jimmy John",
        'date': "January 25th",
        'body': "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Egestas sed tempus urna et pharetra pharetra massa massa ultricies. Iaculis nunc sed augue lacus viverra vitae. Arcu ac tortor dignissim convallis aenean et tortor at risus. Nunc scelerisque viverra mauris in. Nisl nunc mi ipsum faucibus vitae aliquet nec. Ultrices eros in cursus turpis massa. At risus viverra adipiscing at in tellus integer feugiat. Orci a scelerisque purus semper eget duis at tellus at. Libero volutpat sed cras ornare arcu dui vivamus arcu felis."
    }, {

    }

]



@app.route('/')
def home():
    return render_template('index.html', posts=posts)
