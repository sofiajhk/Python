from flask import Flask, request, redirect, render_template, session, flash
# import the Connector function
from mysqlconnection import MySQLConnector
app = Flask(__name__)
# connect and store the connection in "mysql"; note that you pass the database name to the function
mysql = MySQLConnector(app, 'friendsdb')

@app.route('/')
def index():
    query = "SELECT * FROM friends"
    friends = mysql.query_db(query)
    return render_template('index.html', all_friends = friends)

@app.route('/friends', methods=['POST'])
def add():
    #write query as string to add friends into database
    query = "INSERT INTO friends (first_name, last_name, occupation, created_at, updated_at) VALUES (:first_name,:last_name,:occupation, NOW(), NOW())"
    #create a dictionary of data from the POST data we received
    data = {
        'first_name': request.form['first_name'],
        'last_name': request.form['last_name'],
        'occupation': request.form['occupation']
    }
    #run query, with dictionary values injected into the query
    mysql.query_db(query, data)
    return redirect('/')

#to update friend information, create another html page and add a form submitting to following route
@app.route('/update_friend/<friend_id>', methods=['GET', 'POST'])
def update(friend_id):
    if request.method == 'POST':
        query = "UPDATE friends SET first_name = :first_name, last_name = :last_name, occupation = :occupation WHERE id = :id"
        data = {
            'first_name': request.form['first_name'],
            'last_name': request.form['last_name'],
            'occupation': request.form['occupation'],
            'id': friend_id
        }
        mysql.query_db(query, data)
        return redirect('/')
    else:
        query = "SELECT * FROM friends"
        friends = mysql.query_db(query)
        return render_template('update.html', friend_id = int(friend_id), all_friends = friends)

#to remove a friend, you do not need a separate html page, just create another form on index.html that takes value of friend ID that is being removed
@app.route('/remove_friend/<friend_id>', methods=['GET', 'POST'])
def remove(friend_id):
    if request.method == 'POST':
        query = "DELETE FROM friends WHERE id = :id"
        data = {'id': friend_id}
        mysql.query_db(query, data)
        return redirect('/')
    else:
        query = "SELECT * FROM friends"
        friends = mysql.query_db(query)
        return render_template('remove.html', friend_id = int(friend_id), all_friends = friends)
        
app.run(debug=True)
