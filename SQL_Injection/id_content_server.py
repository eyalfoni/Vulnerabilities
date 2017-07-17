from flask import Flask, request, render_template, Response
from flask_mysqldb import MySQL

app = Flask(__name__)
# Dummy password in plaintext
app.config.from_mapping({'MYSQL_USER': 'root', 'MYSQL_PASSWORD': 'admin',
                         'MYSQL_DB': 'id_content_db'})
mysql = MySQL(app)


@app.route('/')
def index():
    return Response('Welcome to the hackable site - go to /login')


@app.route('/userid/<userid>')
def page_content(userid):
    # URL decode userid
    cur = mysql.connection.cursor()
    sql_query = 'SELECT * FROM page WHERE id=' + str(userid)
    print sql_query
    cur.execute(sql_query)
    rv = cur.fetchall()
    print rv
    if not rv:
        return Response('No page content matched id.')
    if rv:
        return Response('Page content succesfully displayed')
