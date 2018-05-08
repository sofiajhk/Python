from flask import Flask, render_template, request, redirect, session
import random 
app = Flask(__name__)
app.secret_key = 'ThisIsSecret'

@app.route('/')
def index():
    if session.has_key('correct_number') == False:
        session['correct_number'] = random.randrange(0,101)
    print session['correct_number']
    return render_template("greatNumberGame.html")

@app.route('/guess', methods=["POST"])
def guess():
    guess = request.form['guess']
    print guess
    #session['guess_status'] = guess
    #setting guess equal to the value of guess submitted from form
    if not len(guess) > 0:
        session['guess_status'] = 'none'
        #it will redirect to localhost:500 if no number is inputed/guessed!
        print "No number was inputed/guessed!"
        return redirect('/')
    if int(guess) > session['correct_number']:
        #int(string) turns value into an integer from a string!
        session['guess_status'] = 'high'
        return redirect('/')
    elif int(guess) < session['correct_number']:
        session['guess_status'] = 'low'
        return redirect('/')
    else:
        #this is if int(guess) == session['correct_number']
        session['guess_status'] = 'correct'
        return redirect('/')

@app.route('/refresh', methods=['POST'])
def refresh():
    session.pop('guess_status')
    session.pop('correct_number')
    session['guess_status'] = 'hide_div'
    print "ALL DATA CLEARED! GOOD TO PLAY AGAIN!"
    return redirect('/')

app.run(debug=True)


