from flask import Flask, request, render_template, Response
from flask_mysqldb import MySQL

app = Flask(__name__)
# Dummy password in plaintext
app.config.from_mapping({'MYSQL_USER': 'root', 'MYSQL_PASSWORD': 'admin',
                         'MYSQL_DB': 'id_content_db'})
mysql = MySQL(app)


@app.route('/')
def index():
    return Response('Welcome to the hackable site - go to /userid/<userid>')


@app.route('/userid/<userid>')
def page_content(userid):
    cur = mysql.connection.cursor()
    sql_query = 'SELECT page_content FROM page WHERE id=' + str(userid)
    print sql_query
    cur.execute(sql_query)
    rv = cur.fetchall()
    print rv
    if not rv:
        return Response('No page content matched id.')
    if rv:
        res = ''
        for elem in rv:
            res += ''.join(elem)
        return Response(res)
