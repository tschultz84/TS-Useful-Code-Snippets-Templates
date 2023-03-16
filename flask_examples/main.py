# This page contains most of the actual functions and routes. 

from flask import request, render_template, Blueprint
import time

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

    # Initialize. 
    python_data=dict()

    # Pull the data.
    value = request.form.get("value")

    if value != None:
        # Output a string. 
        python_data['output_string'] = 'You posted an HTML variable:' + value
    else: python_data['output_string'] = "You haven't yet posted an HTML variable."

    # Pause. This is helpful in the example, but not necessary. Delete in production.  
    time.sleep(2)

    return render_template('jquery_post.html',python_data=python_data)
