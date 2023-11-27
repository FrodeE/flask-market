from flask import Flask
app = Flask(__name__)

# Decorator - one step before app is executed.
@app.route('/') # Our homepage
def hello_world():
    return '<h1>This is a bigger hello world!</h1>'      # Here we can return some HTML

# Dynamic route example
@app.route('/user/<username>')
def about_page(username):
    return f'<h1>This is the user page of {username}</h1>'

