from flask import Flask

app = Flask(__name__)

@app.route("/hello")
def hello():
    """Função hello Word"""
    return "hello world"


# url processors (urls variables). You can use this to handle diferent routes
# in the same function
@app.route('/greet/<name>')
def greet(name):
    if name == "ariel":
        return f"Hello {name} hard balls"
    else:
        return f"hello {name}, u pish of shit"


# url processors (urls variables)> Can also be strong type, so in this exemple
# i saying that number1 and 2 is a int
# if I pass anything other than int, the return will be "NOT FOUND"
@app.route('/add/<int:number1>/<int:number2>')
def add(number1, number2):
    return f'{number1}+{number2}=={number1+number2}'


from flask import request


@app.route('/handle_url_params')
def handle_params():
    # return str(request.args)
    # if I return the string version of request.args without paramters u se
    # that is a empty imutable dictionary.
    # But if I pass a paramter like /handle_url_params?name=mike&greeting=Hello
    # than u get ImmutableMultiDict([('name', 'mike'), ('greeting', 'hello')])

    # You can use this request.args to .get information from URL and return
    # formated like
    greeting = request.args.get('greeting')
    name = request.args.get('name')
    #### return f'{greeting} Sr. {name}'

    # but if one of this args go missing, we get a bad request so is important
    # to check if is not missing, like
    if 'greeting' in request.args.keys() and 'name' in request.args.keys():
        return f'{greeting} Sr. {name}'
    else:
        return "Missing paramters !!!"


# By default all the routes is GET, to use other types of routes you have to
# specify the methods.
@app.route('/hello', methods=['POST', 'DELETE'])
def hello_post():
    # You can work with more than on type of method
    if request.method == "POST":
        return "Hello POST"
    elif request.method == "DELETE":
        return "DELETE World"


# Returning a custom response. Normaly the response comes automaticaly handled
# but we can pass the response.
@app.route('/handwrite_response')
def passing_response():
    return 'passing 500 response by hardwrite\n', 500# so passing a 500 I passing a code that
    # informs that the server not response.
        # like this:
        # > curl -I http://127.0.0.1:5000/custom
        # HTTP/1.1 500 INTERNAL SERVER ERROR
        # Server: Werkzeug/3.0.3 Python/3.11.9
        # Date: Sun, 29 Sep 2024 23:14:20 GMT
        # Content-Type: text/html; charset=utf-8
        # Content-Length: 16
        # Connection: close

# we can also pass custom responses like
from flask import make_response
@app.route('/custom_response')
def custom_response():
    response = make_response("Normal content for GET method\n")
    response.status_code = 202
    response.headers['content-type'] = 'AAAAA: application/octert-stream'
    return response
# And we get the custom response(remembering that we get this information\
    # by using the curl -I link/custom_response):
        # > curl -I http://127.0.0.1:5000/custom_response
        # HTTP/1.1 202 ACCEPTED
        # Server: Werkzeug/3.0.3 Python/3.11.9
        # Date: Sun, 29 Sep 2024 23:20:16 GMT
        # content-type: AAAAA: application/octert-stream
        # Content-Length: 0
        # Connection: close
# If we do the normal GET we will get the information from the\
    # make_response content:
        # > curl http://127.0.0.1:5000/custom_response
        # Normal content for GET method

##### Handdling templates(HTML) and more  ######
from flask import render_template

# You pass the template folder
app = Flask(__name__, template_folder='../frontend/templates/')

# Then you can call html files by name
@app.route("/")
def index():
    return render_template('index.html')

# We can dynamically change things in the HTML file
# Passing keyword values
@app.route("/info_to_html")
def passing_information_to_html():
    myValue = "Dwarf Software"
    reults = 10+20
    myList = [1, 2, 3, 4, 5, 6]
    return render_template('index.html', values=myValue, result=reults,myList=myList)


# We can dynamically change things in the HTML file
# Inheriting pages is usefull to not keeping repeting yourself
@app.route("/inherit_static_pages")
def inherit_static_pages():
    myValue = "Dwarf Software"
    reults = 10+20
    myList = [1, 2, 3, 4, 5, 6]
    return render_template('temp_message.html', values=myValue, result=reults,myList=myList)

# We can dynamically change things in the HTML file
# using filters
@app.route("/filters")
def filters():
    dibresh = 'Hello FILTERS'
    return render_template('filters.html', dibresh=dibresh)

# creating my on custom filter
# this filter reversses the string
@app.template_filter('myFilter')
def reverse_string(myString):
    # reversing the string
    return myString[::-1]
    
# creating my on custom filter
# this filter reversses the string
@app.template_filter('myFilter_repet')
def repeting(s, times=2):
    # You can pass more than one parameter
    # so you can work reciving data
    # reversing the string
    return s*times

# creating my on custom filter
# this filter alnternates between upper and lower case
@app.template_filter('alternating_case')
def alternating_case(s):
    return ''.join([c.upper() if i % 2 == 0 else c.lower() for i,c in enumerate(s)])

# Redirecting endpoints with dynamic URL
from flask import redirect, url_for
@app.route('/redirect_endpoint')
def redirect_endpoint():
    return redirect(url_for('filters'))


# Handdling POST request in a better way. We going to learn to hand forms
# handdling forms data, data with js, how to hand json
from flask import request
@app.route('/ind', methods=['GET', 'POST'])
def index_hand():
    if request.method == 'GET':
        return render_template('index_hand.html')
    elif request.method == 'POST':
        #geting username from the html form
        username = request.form['username']
        # you can also do using get insted of the keyword
        password = request.form.get('password')

        if username == 'menezess42' and password == '1234':
            return 'Nice'
        else:
            return 'Get away hacker'

import pandas as pd
# we can also upload files
@app.route('/fileUpLoad', methods=['POST'])
def file_upload():
    file = request.files['file']
    if file.content_type == 'text/plain':
        file_in_binary = file.read()
        return file_in_binary

    elif file.content_type=="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet" or file.content_type=="application/vnd.ms-excel, text/plain":
        df = pd.read_excel(file.read())
        return df.to_html()


# Reading a excel file, reading the file, displaying like html and return as a csv
from flask import Response


@app.route('/convert_csv', methods=['POST'])
def convert_csv():
    file = request.files['file']
    df = pd.read_excel(file.read())
    # using response imported from flask
    response = Response(
        df.to_csv(),# what I'm responding with (in this case CSV)
        mimetype='text/csv', # Content type
        headers={
            'Content-Disposition': 'attachment; filename=result.csv'
        }
    )
    return response

import os
import uuid
# Reading a excel file, converting to CSV and storing, than feeding
# the user with a Download HTML page so he can download the csv
# this is usefull for data analytics
@app.route('/convert_csv_&_store', methods=['POST'])
def convert_csv_store():
    file = request.files['file']
    df = pd.read_excel(file.read())

    if not os.path.exists('downloads'):
        os.makedirs('downloads')

    filename = f'{uuid.uuid4}.csv'
    df.to_csv(os.path.join('downloads', filename))
    return render_template('download.html', filename=filename)


# this function uses teh send_from_directory to fetch for the file
# in the directory and return back to the user.
from flask import send_from_directory
@app.route('/download/<filename>')
def download(filename):
    return send_from_directory('downloads', filename, download_name='result.csv')


from flask import jsonify
# Handdling POST using JSON and JS
@app.route('/handle_post', methods=['POST'])
def handle_post():
    greeting = request.json['greeting']
    name = request.json['name']

    with open('file.txt', 'w') as f:
        f.write(f'{greeting}, {name}')
    return jsonify({'message': 'Successfully written!'})

##### Static files and Bootstrap #####

app = Flask(__name__, template_folder='../frontend/templates/',
            static_folder="../frontend/static",
            static_url_path="/stc") # you have to pass a URL for static things

@app.route('/index_hello')
def handle_post():
    return render_template('index_hello.html', message='Index')


########################
# Sessions and Cookies #
########################

## Session (are storage in the server side):
from flask import session
# In the real world you have to use a good secret_key
app.secret_key = 'SOME KEY'

@app.route('/set_data')
def set_data():
    session['name'] = 'mike'
    session['other'] = 'AAAA Howrld'
    return render_template('/index_hello.html',message='Sessions data set.')

@app.route('/get_data')
def get_data():
    if 'name' in session.keys() and 'other' in session.keys():
        name = session['name']
        other = session['other']
        return render_template('index_hello.html', message=f'Name:{name} Other:{other}')
    else:
        return ''
#### Alll the script above is hepening in the server side, this is usefull
#### for sensitive information, because all the informatin stays in the server
### and not the user machine

# How to clear a session
@app.route('/clear_session')
def clear_session():
    session.clear()
    return render_template('index_hello.html', message='Session Cleared')

## Cookies (are storege in the client side)
# At the cookie is in the client side, we have to instruc the browser on
# how to set the cookie in the client side
@app.route('/set_cookie')
def set_cookie():
    response = make_response(render_template('index_hello.html', message='Cookie set.'))
    response.set_cookie('cookie_name','cookie_value')
    return response

@app.route('/get_cookie')
def get_cookie():
    cookie_value = request.cookies['cookie_name']
    return render_template('index_hello.html', message=f'Cookie Value: {cookie_value}')


@app.route('/remove_cookie')
def remove_cookie():
    response = make_response(render_template('index_hello.html', message='Cookie Removed.'))
    response.set_cookie('cookie_name',expires=0)
    return response
####

## Message flashing (Display a message that flash)
from flask import request,flash
@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'GET':
        return render_template('login.html')
    elif request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')
        if username == 'menezess42' and password=='1234':
            flash('Successful Login!')
            return render_template('index_hello.html', message='')
        else:
            flash('Login fail')
            return render_template('index_hello.html', message='')
            


if __name__ == '__main__':
    app.run(debug=True)

