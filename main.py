#!/usr/bin/env python
from pprint import pprint as pp
from flask import Flask, flash, redirect, render_template, request, url_for
import requests
from flask import request


app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():

    error = False
    cat_fact = ""

    if(request.form.get('animal')):
        try:
            cat_fact = requests.get('https://cat-fact.herokuapp.com/facts/random?animal_type='+request.form.get('animal')).json()
        except:
            error = True
    else:
        cat_fact = requests.get('https://cat-fact.herokuapp.com/facts/random?animal_type=cat').json()
    
    cat_image = requests.get('https://api.thecatapi.com/v1/images/search', 
                headers={"x-api-key":"9d3b38de-757e-41ca-b77a-603d16f52442"}).json()

    return render_template('fact.html', 
        cat_image=cat_image[0],
        cat_fact=cat_fact,
        error=error,
        animal=request.form.get('animal')
    )

# cat_breeds = requests.get('https://api.thecatapi.com/v1/breeds', 
#             headers={"x-api-key":"9d3b38de-757e-41ca-b77a-603d16f52442"}).json()
if __name__=='__main__':
    app.run(host='0.0.0.0', port=20581, debug=True)
