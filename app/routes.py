from app import app
from flask import Flask, render_template, request, redirect, url_for
import requests
import json
import os
import pandas as pd
from bs4 import BeautifulSoup
from app.utils import get_element, selectors

@app.route("/")
@app.route("/main")
def main():
    return render_template("main.html")

@app.route("/extraction", methods=['POST', 'GET'])
def extraction():
    if request.method == 'POST':
        url = f"https://www.ceneo.pl/{product_code}#tab=reviews"
        all_opinions = []
        while(url):
            print(url)
            response = requests.get(url)
            page_dom = BeautifulSoup(response.text, "html.parser")
            opinions = page_dom.select("div.js_product-review")
            for opinion in opinions:
                single_opinion = {}
                for key, value in selectors.items():
                    single_opinion[key] = get_element(opinion, *value)
                all_opinions.append(single_opinion)
            try:    
                url = "https://www.ceneo.pl"+get_element(page_dom,"a.pagination__next","href")
            except TypeError:
                url = None
        if not os.path.exists("./app/data/opinions"):
            os.mkdir("./app/data/opinions")
        with open(f"./app/data/opinions/{product_code}.json", "w", encoding="UTF-8") as jf:
            json.dump(all_opinions, jf, indent=4, ensure_ascii=False)
    return render_template("extraction.html")

@app.route("/product_list")
def product_list():
    return render_template("p_list.html")

@app.route("/product")
def product():
    return render_template("product.html")