# This page contains most of the actual functions and routes. 

from flask import request, render_template, Blueprint
import time
import pandas as pd
import json
import os

main = Blueprint('main',__name__)


@main.route('/')
def index():

    # Initialize. 
    python_data=dict()

    # Output a string. 
    python_data['output_string'] = 'Hello world! Welcome to the empty Python Flask app.'
    
    return render_template('index.html',python_data=python_data)


@main.route('/jquery_post', methods=["GET","POST"])
def jquery_post():

    # Pause. This is helpful in the example, but not necessary. Delete in production.  
    time.sleep(2)

    # Initialize. 
    python_data=dict()

    # Pull the data.
    value = request.form.get("value")

    print(f"Value of POST variable is {value}!")

    if value != None:
        # Output a string. 
        python_data['output_string'] = 'You posted an HTML variable with:' + value
    else: python_data['output_string'] = "You haven't yet posted an HTML variable."

    return render_template('jquery_post.html',python_data=python_data)

# This page shows how to add a row to a form. 
@main.route('/js_add_form_row', methods=["GET","POST"])
def js_add_form_row():
    
    python_data=dict()

    # Pull the data.
    valuedict = request.args

    print(f"Value of POST variable is {valuedict}!")

    if valuedict != None:
        # Output a string. 
        python_data['output_string'] = 'You posted an HTML variable with some data.'
        python_data['out_dict'] = valuedict
    else: python_data['output_string'] = "You haven't yet posted an HTML variable."

    return render_template('js_add_form_row.html',python_data=python_data)

    

# Functional Flask / CRUD application writing to/from a CSV file.
@main.route('/jquery_crud', methods=["GET","POST"])
def jquery_crud():
    
    # Initialize.
    python_data=dict()
    python_data['output_string'] = "Viewing jquery_crud route from Python Flask."

    # Retrieve tabular data, then convert it into JSON.
    # These following lines of code are replaced in real life, for example if you retrieve from PostGreSQL, you need to re-write this code to serialize into JSON.
    absolute_path = os.path.dirname(__file__)
    file_path = os.path.join(absolute_path,"static/recipes.csv")
    tabular_df = pd.read_csv(file_path)
    tabular_json = tabular_df.to_json()

    # Serialize into JSON.
    python_data['json_out'] = json.dumps(tabular_json)

    # Pull the data.
    valuedict = request.args

    print(f"Value of POST variables are {valuedict}!")

    return render_template('jquery_crud.html',python_data=python_data)