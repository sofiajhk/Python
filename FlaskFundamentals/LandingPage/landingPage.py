from flask import Flask, render_template, request, redirect
app = Flask(__name__)

@app.route('/')
#this will be our root route
def index():
    return render_template('index.html')

@app.route('/ninjas')
#this route demonstrates how to access static files (CSS, JavaScript, img) through our html file
def aboutNinjas():
    return render_template('ninjas.html')

@app.route('/dojos/new')
#this route demonstrates how to make forms and POST information to server
#(needs two app.routes - one to render the html file and another to POST information)
#don't forget to import "request" and "redirect" in line 1!
def dojos():
    return render_template('dojos.html')
@app.route('/users', methods=['POST'])
def createUser():
    print "New User Has Signed Up!"
    name = request.form['name']
    email = request.form['email']
    return redirect('/dojos/new')

app.run(debug=True)