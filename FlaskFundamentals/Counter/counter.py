from flask import Flask, render_template, request, redirect, session
app = Flask(__name__)
app.secret_key = 'ThisIsSecret'
#you need a secret key for security purposes!

@app.route('/')
def index():
    if session.has_key('counter') == False:
        session['counter'] = 1
        #this makes it so initial load is set at 1
    else:
        session['counter'] += 1
        #this makes it so each refresh adds 1 to the counter
    return render_template("index.html", counter=session['counter'])

@app.route('/button', methods=['POST'])
def increment():
    if request.form['action'] == '+2':
        session['counter'] += 1
        #only +=1, not 2 because the redirect already refreshes page and
        #the index() function already adds one, so together it is 2
    elif request.form['action'] == "reset":
        session['counter'] = 0
    return redirect('/')

    #must have if statement in POST '/button' route to check which form is being submitted 
    #since they have both submit to same place with same name but different values!
    #refer to hidden inputs in flask chapter!

app.run(debug=True)
