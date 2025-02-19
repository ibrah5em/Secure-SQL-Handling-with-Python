# import the library for SQL Server 
import pyodbc as odbc
# Making the connection as string to send it to the DB
Connection = (
    r'DRIVER={SQL Server};'
    r'SERVER=X\SQLEXPRESS;'
    'DATABASE=myDB;'
    'Trusted_Connection=yes;'
)
# Connect to the database
Conn = odbc.connect(Connection)
# imoport some modules for HTTP requests and filtering data.
from flask import Flask, render_template, request
import re
# making flusk know the module 
app = Flask(__name__)
# define the root folder
@app.route('/')
# index() function that make the user return to the index.html 
def home():
    return render_template('index.html')
# accepts POST requests.
@app.route('/login', methods=['POST'])
def login():
    username = request.form['username']
    password = request.form['password']

    # Validate input using regex to prevent SQL injection
    if not re.match(r'^[a-zA-Z0-9_]+$', username):
        return 'Invalid username format'
    if not re.match(r'^[a-zA-Z0-9_]+$', password):
        return 'Invalid password format'
    # Database Connection and Query Execution
    conn = odbc.connect(Connection)
    cursor = conn.cursor()
    query = "SELECT * FROM users WHERE username = ? AND password = ?"
    cursor.execute(query, (username, password))
    # Check the Query Result
    result = cursor.fetchone()
    if result:
        return 'Logged in successfully'
    else:
        return 'Invalid credentials'

# Run the Flask Application
if __name__ == '__main__':
    app.run(debug=True)
