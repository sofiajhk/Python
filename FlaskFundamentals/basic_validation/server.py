from flask import Flask, render_template, redirect, request, session, flash
app = Flask(__name__)
app.secret_key = 'KeepItSecretKeepItSafe'

@app.route('/')
def index():
    return render_template('index.html')

#using len() to display validation error/success!
    # @app.route('/process', methods=['POST'])
    # def process():
    #     #do some validations here!
    #     if len(request.form['name']) < 1:
    #         print "there was no input"
    #     else:
    #         print "success!"
    #     return redirect('/')

#using flash messages on the server/refer to view(HTML) to see client-side
@app.route('/process', methods=['POST'])
def process():
    if len(request.form['name']) < 1:
        flash("Name cannot be empty!") #passing a string to flash function
    else:
        flash("Success! Your name is {}".format(request.form['name']))
    return redirect('/')

app.run(debug=True)