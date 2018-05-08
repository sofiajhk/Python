from flask import Flask, render_template, request, redirect, flash
from mysqlconnection import MySQLConnector
import re

app = Flask(__name__)
mysql = MySQLConnector(app,'email_validation')
EMAIL_REGEX = re.compile(r'^[\w\.+_-]+@[\w\._-]+\.[\w]*$')
app.secret_key = 'ThisIsSecret'

def validate(email):
    # Return whether or not the email passed in is valid
    return EMAIL_REGEX.match(email)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        if(validate(request.form['email'])):
            query = "INSERT INTO emails (email, created_at) VALUES (:email, NOW());"
            data = {'email': request.form['email']}
            mysql.query_db(query, data)
            flash("Success! You submitted the email {}".format(request.form['email']))
            return redirect('/success')
        else:
            flash("The email address is not valid!")
    return render_template('index.html')

@app.route('/success')
def success():
    query = "SELECT * FROM emails;"
    emails = mysql.query_db(query)
    return render_template('success.html', emails = emails)

@app.route('/<id>', methods=['POST'])
def remove(id):
    query = "DELETE FROM emails WHERE id = :id;"
    data = {'id': id}
    mysql.query_db(query,data)
    flash('Sucessfully removed email!')
    return redirect('/success')

app.run(debug=True)