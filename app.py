from flask import Flask, render_template, url_for


app = Flask(__name__)


@app.route('/')
def index():

    return render_template('index.html', page='home')

@app.route('/')
def projects():

    return render_template('projects.html', page='projects')

@app.route('/')
def contact():

    return render_template('contact.html', page='contact')
