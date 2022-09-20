from flask import Flask, render_template
app = Flask(__name__)

#########################

posts = [
    {
        'title': "Clerks 3 Released!",
        'image': "https://media.vanityfair.com/photos/611bd8b39327f496d8579bc1/1:1/w_1188,h_1188,c_limit/vf-first-look-clerks-3-b.jpg",
        'author': "Ben Affleck",
        'date': "9/16/22",
        'body': "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Vestibulum lectus mauris ultrices eros in cursus turpis. Est ultricies integer quis auctor elit sed vulputate. Turpis egestas pretium aenean pharetra magna. Velit aliquet sagittis id consectetur. Vulputate ut pharetra sit amet aliquam id diam. Hendrerit gravida rutrum quisque non tellus. Neque gravida in fermentum et sollicitudin ac orci. Aliquam purus sit amet luctus. Posuere sollicitudin aliquam ultrices sagittis orci a scelerisque purus semper. Accumsan sit amet nulla facilisi morbi tempus iaculis urna. Eu feugiat pretium nibh ipsum consequat nisl vel pretium. Sagittis vitae et leo duis ut diam. In ornare quam viverra orci. Varius quam quisque id diam vel quam elementum pulvinar etiam."
    }, 
    {
        'title': "Clerks 2 Released!",
        'image': "https://resizing.flixster.com/68TbItepdcLsBe2wJTjwZUCAj9Y=/300x300/v2/https://flxt.tmsimg.com/assets/p161259_k_h9_aa.jpg",
        'author': "Jay Mewes",
        'date': "07/21/06",
        'body': "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Aliquam id diam maecenas ultricies mi eget. Faucibus in ornare quam viverra orci sagittis eu volutpat odio. Risus feugiat in ante metus dictum at tempor commodo. Quam lacus suspendisse faucibus interdum posuere lorem ipsum. Risus nec feugiat in fermentum posuere urna nec tincidunt praesent. In eu mi bibendum neque egestas congue. Viverra maecenas accumsan lacus vel. Dui id ornare arcu odio ut sem nulla. Imperdiet dui accumsan sit amet nulla facilisi morbi tempus iaculis. Egestas dui id ornare arcu odio ut. Cras pulvinar mattis nunc sed blandit. Volutpat sed cras ornare arcu dui vivamus. Nulla pellentesque dignissim enim sit amet venenatis. Est lorem ipsum dolor sit amet consectetur adipiscing. Adipiscing commodo elit at imperdiet dui accumsan sit. Vivamus arcu felis bibendum ut tristique."
    }, 
    {
        'title': "Animated Series Released!",
        'image': "https://comicvine.gamespot.com/a/uploads/square_medium/13/135098/6875582-clerkstas.jpg",
        'author': "Scott Mosier",
        'date': "5/31/00",
        'body': "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Tellus cras adipiscing enim eu turpis egestas pretium aenean. Et leo duis ut diam quam nulla. Pellentesque elit eget gravida cum sociis. Molestie ac feugiat sed lectus vestibulum mattis ullamcorper velit sed. Lorem mollis aliquam ut porttitor leo a diam sollicitudin. Molestie nunc non blandit massa. Enim ut tellus elementum sagittis vitae et. Tincidunt eget nullam non nisi est sit amet. Arcu felis bibendum ut tristique et egestas quis. Vel pharetra vel turpis nunc eget lorem dolor sed viverra. Mauris pellentesque pulvinar pellentesque habitant morbi tristique senectus et. Morbi blandit cursus risus at ultrices mi tempus imperdiet nulla."
    }, 
    {
        'title': "Clerks Released!",
        'image': "https://resizing.flixster.com/Hd2DDT15u5zjTbfZLtvLqj0E-Uw=/300x300/v2/https://flxt.tmsimg.com/assets/p15365_v_v12_ag.jpg",
        'author': "Kevin Smith",
        'date': "10/19/94",
        'body': "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Neque aliquam vestibulum morbi blandit cursus risus at ultrices mi. Magna fermentum iaculis eu non. Arcu non sodales neque sodales ut etiam sit amet. Interdum velit euismod in pellentesque. Sit amet consectetur adipiscing elit pellentesque habitant morbi. Egestas fringilla phasellus faucibus scelerisque eleifend donec. Proin sed libero enim sed faucibus turpis in eu. Laoreet non curabitur gravida arcu ac tortor. Pulvinar neque laoreet suspendisse interdum consectetur libero id faucibus. Quis varius quam quisque id. Eu consequat ac felis donec et odio pellentesque diam. Viverra justo nec ultrices dui sapien eget mi proin sed. Volutpat ac tincidunt vitae semper quis lectus nulla at. Mattis vulputate enim nulla aliquet porttitor lacus luctus accumsan tortor."
    } 
]



#########################

# localhost:5000
@app.route('/')
def home():
    return render_template('index.html', posts=posts)

@app.route('/about/')
def about():
    return render_template('about.html')

@app.route('/contact/')
def contact():
    return render_template('contact.html')