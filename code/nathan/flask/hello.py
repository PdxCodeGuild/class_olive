from flask import Flask, render_template
app = Flask(__name__)

posts = [
    {
        'picture': ".\static\cow.png",
        'picture_alt': "cow",
        'title': "How to win a race.",
        'body': "Here is an article on how to win a race. It's important to run fast. Also... Godfather ipsum dolor sit amet. That's my family Kay, that's not me. I'm gonna make him an offer he can't refuse. What's the matter with you? Is this what you've become, a Hollywood finocchio who cries like a woman? Oh, what do I do? What do I do? What is that nonsense? Ridiculous! I have a sentimental weakness for my children and I spoil them, as you can see. They talk when they should listen.",
        'author': "John Doe",
        'date': "September 13, 2022"
    }, 
    {
        'picture': ".\static\elk.png",
        'picture_alt': "elk",
        'title': "How to win the lottery.",
        'body': "Here is an article on how to win the lottery. It's important to buy a lottery ticket. Also.... Fredo, you're my older brother, and I love you. But don't ever take sides with anyone against the Family again. Ever. Don Corleone, I am honored and grateful that you have invited me to your home on the wedding day of your daughter. And may their first child be a masculine child. If anything in this life is certain, if history has taught us anything, it is that you can kill anyone. You talk about vengeance. Is vengeance going to bring your son back to you? Or my boy to me? I want your answer and the money by noon tomorrow. And one more thing. Don't you contact me again, ever. From now on, you deal with Turnbull.",
        'author': "Bill Doe",
        'date': "September 5, 2022"
    }, 
    {
        'picture': ".\static\pronghorn.png",
        'picture_alt': "pronghorn antelope",
        'title': "How to win a chess match.",
        'body': "Here is an article on how to win a chess match. It's important to put the king in check. Also.... Vito, how do you like my little angel? Isn't she beautiful? Is that why you slapped my brother around in public? My father's name was Antonio Andolini... and this is for you. It's a Sicilian message. It means Luca Brasi sleeps with the fishes. I am sorry. What happened to your father was business. I have much respect for your father. But your father, his thinking is old-fashioned. You must understand why I had to do that. Now let's work through where we go from here.",
        'author': "Jim Doe",
        'date': "August 13, 2022"
    },
    {
        'picture': ".\static\warpon.png",
        'picture_alt': "tarpon fish",
        'title': "How to get a dog.",
        'body': "Here is an article on how to get a dog. It's important to buy one. Alos.... Why do you hurt me, Michael? I've always been loyal to you. Fredo, you're my older brother, and I love you. But don't ever take sides with anyone against the Family again. Ever. Only don't tell me you're innocent. Because it insults my intelligence and makes me very angry. My father taught me many things here - he taught me in this room. He taught me: keep your friends close, but your enemies closer. You talk about vengeance. Is vengeance going to bring your son back to you? Or my boy to me?",
        'author': "Emily Doe",
        'date': "August 5, 2022"
    }
]

about_me = "Hello I am the creator of this blog. I created this blog to learn flask and better my html/css skills. Things for visiting."

contact_info = {
    'Name': 'Nate',
    'Phone Number': '555-555-5555',
    'Email': 'nate@fake.com'
}

@app.route('/')
def index():
    return render_template("index.html", posts = posts)

@app.route('/about')
def about():
    return render_template("about.html", about_me = about_me)

@app.route('/contact')
def contact():
    return render_template("contact.html", contact = contact_info)








