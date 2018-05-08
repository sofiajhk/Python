from flask import Flask, render_template, request, redirect, session
import random
from datetime import datetime #import time

app = Flask(__name__)
app.secret_key = 'ThisIsSecret'


@app.route('/')
def index():
    if session.has_key('gold_count') == False:
        session['gold_count'] = 0
    if session.has_key('activity') == False:
        session['activity'] = []
        print datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        #this prints the data/time in the string format 2018-5-15 12:24:04
    return render_template("ninjaGold.html")

@app.route('/process_money', methods=['POST'])
def gold_count():
    if request.form['building'] == 'farm':
        gold = random.randrange(10,21)
        session['gold_count'] += gold
        session['activity'].append("Nice, the ninja found "+str(gold)+" gold from the farm! "+str(datetime.now().strftime('%Y-%m-%d %H:%M:%S')))
    elif request.form['building'] == 'cave':
        gold = random.randrange(5,11)
        session['gold_count'] += gold
        session['activity'].append("Wow, the ninja found "+str(gold)+" gold from the cave! "+str(datetime.now().strftime('%Y-%m-%d %H:%M:%S')))
    elif request.form['building'] == 'house':
        gold = random.randrange(2,6)
        session['gold_count'] += gold
        session['activity'].append("Cool, the ninja found "+str(gold)+" gold from the house! "+str(datetime.now().strftime('%Y-%m-%d %H:%M:%S')))
    else:
        #this is for a casino! you have to first determine if it's a win or loss
        winLose = random.randint(0,1)
        #this will return integer I so that 0 <= I <= 1
        if winLose == 1:
            gold = random.randrange(0,51)
            session['gold_count'] += gold
            session['activity'].append("Awesome, the ninja won "+str(gold)+" gold from the casino! "+str(datetime.now().strftime('%Y-%m-%d %H:%M:%S')))
        else:
            gold = random.randrange(0,51)
            session['gold_count'] -= gold
            session['activity'].append("Oh no, the ninja lost "+str(gold)+" gold from the casino! "+str(datetime.now().strftime('%Y-%m-%d %H:%M:%S')))
    return redirect('/')

@app.route('/reset', methods=["POST"])
def reset():
    session.clear()
    #this clears ALL things in the current session
    return redirect('/')

app.run(debug=True)