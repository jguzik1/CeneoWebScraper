from app import app
from flask import Flask, render_template

@app.route("/")
@app.route("/main")
def main():
    return render_template("main.html")

@app.route("/extraction")
def extraction():
    return render_template("extraction.html")

@app.route("/product_list")
def product_list():
    return render_template("p_list.html")

@app.route("/product")
def product():
    return render_template("product.html")