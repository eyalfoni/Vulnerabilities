from __future__ import print_function
from flask import Flask, request, render_template, Response
from flask_mysqldb import MySQL
import sys

app = Flask(__name__)
# Dummy password in plaintext
app.config.from_mapping({'MYSQL_USER': 'root', 'MYSQL_PASSWORD': 'admin',
                         'MYSQL_DB': 'hacking_db'})
mysql = MySQL(app)

app_db = Flask('temp')
app_db.config.from_mapping({'MYSQL_USER': 'root', 'MYSQL_PASSWORD': 'admin',
                            'MYSQL_DB': 'id_content_db'})
mysql_db = MySQL(app_db)


@app.route('/login', methods=['POST', 'GET'])
def login():
    error = None
    if request.method == 'POST':
        return valid_login(request.form['username'],
                           request.form['password'])
    return render_template('login.html', error=error)


@app.route('/')
def index():
    return Response('Welcome to the hackable site - go to /login')


def valid_login(username, password):
    cur = mysql.connection.cursor()
    sql_query = 'SELECT * FROM users WHERE username=\'' + str(username) + \
        '\' and (password=\'' + str(password) + '\')'
    # print(sql_query, sys.stdout)
    cur.execute(sql_query)
    rv = cur.fetchall()
    # print(rv, sys.stdout)
    if not rv:
        return Response('Incorrect credentials. Access denied.')
    else:
        return Response('Correct credentials. Access granted.')
