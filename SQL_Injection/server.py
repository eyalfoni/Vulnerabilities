from flask import Flask, request, render_template, Response
from flask_mysqldb import MySQL

app = Flask(__name__)
# Dummy password in plaintext
app.config.from_mapping({'MYSQL_USER': 'root', 'MYSQL_PASSWORD': 'admin',
                         'MYSQL_DB': 'hacking_db'})
mysql = MySQL(app)


@app.route('/login', methods=['POST', 'GET'])
def login():
    error = None
    if request.method == 'POST':
        return valid_login(request.form['username'],
                           request.form['password'])
    # the code below is executed if the request method
    return render_template('login.html', error=error)


@app.route('/')
def index():
    return Response('Welcome to the hackable site - go to /login')


def valid_login(username, password):
    cur = mysql.connection.cursor()
    # select * from users where username="john" and password="doe"
    sql_query = 'SELECT * FROM users WHERE username=\'' + str(username) + \
        '\' and password=\'' + str(password) + '\''
    cur.execute(sql_query)
    rv = cur.fetchall()
    if not rv:
        return Response('Incorrect credentials. Access denied.')
    else:
        return Response('Correct credentials. Access granted.')
