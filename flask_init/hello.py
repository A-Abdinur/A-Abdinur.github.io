import os

from flask import Flask, url_for, request, render_template, redirect
app = Flask(__name__)

# @app.route('/')
# def index():
#     return url_for('show_user_profile',username='jorge')
    
# @app.route('/user/<username>') #taking variable from the decorator to be used
# def show_user_profile(username):
#     # show the user profile for that user
#     return "User " +str(username)
@app.route('/index/<name>')
@app.route('/index') #changing the access point for the webpage
def index(name=None):
    return render_template('index.html', template_name = name)
    
@app.route('/login', methods = ['GET', 'POST'])
def login():
    error = None
    if request.method == 'POST':
        if valid_login(request.form["username"], request.form["password"]):
            return redirect(url_for('welcome', username=request.form.get('username')), code=200) #for the username index in the request.values dictionary we return the data otherwise we request is from user
        else:
            error = 'Incorrect username and password'
    return render_template('login.html', error = error) #when rendering, you can return any error messages
# @app.route('/post/<int:post_id>')
# def show_post(post_id):
#     return 'Post ' +str(post_id)    

def valid_login(username, password):
    if username == password:
        return True
    else:
        return False    
    
@app.route('/welcome/<username>')
def welcome(username):
    return render_template('welcome.html', username=username)

if __name__ == '__main__':
    host = os.getenv('IP', '0.0.0.0')
    port = int(os.getenv('PORT', 5000))
    app.debug = True
    app.run(host=host, port=port) #creates server waiting for a hit of the address and routes its to matching 