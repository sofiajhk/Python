from flask import Flask, render_template, request, redirect, session, flash
app = Flask(__name__)
app.secret_key = 'ThisIsSecret'

@app.route('/')
def dojoSurvey():
    return render_template("surveyValidation.html")

@app.route('/process', methods=['POST'])
def process():
    if len(request.form['name']) < 1 or len(request.form['comments']) < 1:
        flash("All fields must be filled in!")
    elif len(request.form['comments']) > 120:
        flash("Comments section is more than 120 characters!")
    else:
        print "Got Post Info!"
        flash("Thank you {}! You have successfully filled out the form!".format(request.form['name']))
        session['name'] = request.form['name']
        session['location'] = request.form['location']
        session['language'] = request.form['language']
        session['comments'] = request.form['comments']
    return redirect('/')

@app.route('/results')
def results():
    return render_template("surveyResult.html")

app.run(debug=True)