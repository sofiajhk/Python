from flask import Flask, render_template, redirect, request, session, flash
import re
#the "re" module will let us perform some regular expression operations
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
#create a regular expression object that we can use operations on
app = Flask(__name__)
app.secret_key = 'ThisIsSecret'

@app.route('/')
def index():
    return render_template("index.html")

#using regex to match a string that follows a pattern (in this case, an email address)
@app.route('/process', methods=['POST'])
def submit():
    if len(request.form['email']) < 1:
        flash("email cannot be blank!")
    elif not EMAIL_REGEX.match(request.form['email']):
    #else if email doens't match regular express display "invalid email address" message
        flash("invalid email address!")
    else:
        flash("success! your email is {}".format(request.form['email']))
    return redirect('/')

app.run(debug=True)