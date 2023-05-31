from app import app
from flask import Flask, render_template

@app.route("/")
def home():
    return render_template('main.html')
@app.route("/index")
def index():
    return "Hello World"

@app.route("/name", defaults={'name': "Anonim"})
@app.route("/name/<name>")
def name(name):
    return f"Hello {name}"