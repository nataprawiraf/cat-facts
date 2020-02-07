#!/usr/bin/env python
from pprint import pprint as pp
from flask import Flask, flash, redirect, render_template, request, url_for
import requests

app = Flask(__name__)

@app.route('/')
def index():
    cat_image = requests.get('https://api.thecatapi.com/v1/images/search', headers={"x-api-key":"9d3b38de-757e-41ca-b77a-603d16f52442"}).json()
    cat_breeds = requests.get('https://api.thecatapi.com/v1/breeds', headers={"x-api-key":"9d3b38de-757e-41ca-b77a-603d16f52442"}).json()
    pp(cat_image)
    return render_template('fact.html', cat_image=cat_image[0], cat_breeds=cat_breeds)

if __name__=='__main__':
    app.run(host='0.0.0.0', port=20800, debug=True)
