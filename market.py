from flask import Flask, render_template
app = Flask(__name__)

# Decorator - one step before app is executed.
@app.route('/') # Our homepage
@app.route('/home')
def home_page():
    return render_template('home.html')

# Dynamic route example
@app.route('/about/<username>')
def about_page(username):
    return render_template('about.html', name=username)

