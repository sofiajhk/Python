from flask import Flask, render_template, request, redirect
app = Flask(__name__)

@app.route('/')
def dojoSurvey():
    return render_template("dojosurvey.html")

@app.route('/process', methods=['POST'])
def process():
    print "Got Post Info"
    name = request.form['name']
    location = request.form['location']
    language = request.form['language']
    comments = request.form['comments']
    return render_template("surveyResult.html", name=name, location=location, language=language, comments=comments)
    #another method...
    #return redirect('/submit/' + name + '/'+ location + '/' + language + '/' + comment)

# @app.route('/submit/<name>/<location>/<language>/<comments>')
# def submit(name, location, language, comments):
#     print name
#     print location
#     print language
#     print comments
#     return redner_template
#     return render_template('submit.html', name=name, location=location, language=language, comment=comment)

app.run(debug=True)