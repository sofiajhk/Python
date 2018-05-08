from flask import Flask, render_template, redirect, request, session, flash
from mysqlconnection import MySQLConnector
import re
import md5

app = Flask(__name__)
mysql = MySQLConnector(app,'login_registration')
app.secret_key = 'ThisIsSecret'

EMAIL_REGEX = re.compile(r'^[\w\.+_-]+@[\w\._-]+\.[\w]*$')

@app.route('/')
def index():
    query = "SELECT * FROM users"
    users = mysql.query_db(query)
    print "index method: found", len(users), "users in the db"
    # show how many users are in the database in the terminal
    return render_template('index.html')

@app.route('/success')
def success():
    if 'id' not in session:
        return redirect('/')
    else:
        user_query = "SELECT * FROM users WHERE id = :id"
        user_data = {'id': session['id']}
        users = mysql.query_db(user_query, user_data)
        current_user = users[0]
        return render_template('success.html', user = current_user)

@app.route('/register', methods=['POST'])
def register():
    print request.form
    # practice using an errors list to save error message (to flash later)
    errors = []

    if len(request.form['first_name']) < 2:
        errors.append('First Name must be longer than 2 letters')
    elif not request.form['first_name'].isalpha():
        errors.append('First Name can only contain letters')

    if len(request.form['last_name']) < 2:
        errors.append('Last Name must be longer than 2 letters')
    elif not request.form['last_name'].isalpha():
        errors.append('Last Name can only contain letters')

    if not EMAIL_REGEX.match(request.form['email']):
        errors.append('Email is not valid')

    if not len(request.form['password']) >= 8:
        errors.append('Password must be at least 8 characters')
    elif not request.form['pw_conf'] == request.form['password']:
        errors.append('Password and Confirmation do not match')

    # if we have errors, use if/for statement to flash them 
    # and exit function to prevent saving bad data to database!
    if errors:
        for error in errors:
            flash(error)
        return redirect('/')
    else:
        # if NO ERRORS, encrypt the password and save user info
        # the following encrypts pw provided as 32 character string
        # MAKE SURE TO HASH PW BEFORE YOU STORE IN DB
        hashed_pw = md5.new(request.form['password']).hexdigest()
        user_data = {
            'first_name': request.form['first_name'],
            'last_name': request.form['last_name'],
            'email': request.form['email'],
            'password': hashed_pw
        }
        # print user_data to check that all data is correct
        print user_data
        # the triple """ in query statement allows you to have spaces in your query
        register_query = "INSERT INTO users (first_name, last_name, email, password, created_at, updated_at) VALUES (:first_name, :last_name, :email, :password, NOW(), NOW())"
        new_user = mysql.query_db(register_query, user_data)
        print new_user
        # the "is not 0" statement checks to make sure new_user is not null
        if new_user is not 0:
            session['id'] = new_user
        else:
            flash('Registration Failed')
        return redirect('/success')

@app.route('/login', methods=['POST'])
def login():
    # create request.form keys to variable (email/password) to prevent repetitively typing them out
    email = request.form['email']
    password = request.form['password']

    # run validations to check if user exists in database
    if not EMAIL_REGEX.match(email):
        flash('Email is not valid')

    if not len(password) >= 8:
        flash("Password is not valid")

    # if no errors/flashe messages, run the following query to database
    if not '_flashes' in session:
        try:
            # this will not run unless the email submitted exists in db
            login_query = 'SELECT * FROM users WHERE email = :email'
            login_data = {'email': email}
            user = mysql.query_db(login_query, login_data)
            hashed = user[0]['password']
            # user[0]['password'] is the value of the hashed pw from the user with the matching email
            if hashed == md5.new(password).hexdigest():
            # checking if hashed pw matches login password
                session['id'] = user[0]['id']
                print "login success!"
                return redirect('/success')
        except:
            flash('Invalid username or password')
    return redirect('/')    

app.run(debug=True)