from flask import Flask, render_template, request, redirect, session, flash
import re
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
PW_REGEX = re.compile(r'^([^0-9]*|[^A-Z]*)$')
#to check if pw contains one number and one uppercase letter!
app = Flask(__name__)
app.secret_key = 'ThisIsSecret'

@app.route('/')
def index():
    return render_template("RegistrationForm.html")

@app.route('/process', methods=['POST'])
def process():
    if len(request.form['fname']) < 1 or len(request.form['lname']) < 1 or len(request.form['email']) < 1 or len(request.form['password']) < 1 or len(request.form['cpassword']) < 1:
        flash("All fields must be filled in!", 'error')
    elif str.isalpha(str(request.form['fname'])) != True or str.isalpha(str(request.form['lname'])) != True:
        flash("First and Last Name cannot contain any numbers!", 'error')
    elif not EMAIL_REGEX.match(request.form['email']):
        flash('Invalid Email Address!', 'error')
    elif len(request.form['password']) <= 8:
        flash('Password must be at least 8 characters!', 'error')
    elif PW_REGEX.match(request.form['password']):
        flash('Password requires one uppercase letter and one number!', 'error')
    elif request.form['password'] != request.form['cpassword']:
        flash('Passwords do not match!', 'error')
    else:
        print "Got Post Info!"
        flash("Thank you {}! You have successfully filled out the form!".format(request.form['fname']), 'success')
        session['fname'] = request.form['fname']
        session['lname'] = request.form['lname']
        session['email'] = request.form['email']
        session['password'] = request.form['password']
    return redirect('/')

@app.route('/results')
def results():
    return render_template("formResult.html")

app.run(debug=True)